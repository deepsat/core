import asyncio
from rtcbot import CVCamera
from rtcbot.arduino import SerialConnection
import numpy as np
import cv2
from datetime import datetime
from openvino.inference_engine import IECore, IENetwork
from models import IEModel
import os
from time import time
import json

w, h = 1600, 1200
w_roads, h_roads = 1792, 1280


class Core:
    def __init__(self):
        self.device = "MYRIAD"
        self.ie = IECore()
        self.roads = IEModel("models/roads.xml",
                             "models/roads.bin",
                             self.ie,
                             self.device,
                             num_requests=7,
                             batch_size=5)
        # self.objects = IEModel("models/yolo_tiny.xml", "models/yolo_tiny.bin",
        #                        self.ie, self.device, 1)
        self.loop = asyncio.get_event_loop()
        self.camera = CVCamera(1600, 1200, fps=2, loop=self.loop)
        self.arduino = SerialConnection(
            "/dev/serial0",
            readFormat="< 3f 3f 3f 3f 3B H 3B ? B 5f B H L",
            readKeys=[
                "temperature", "pressure", "altitude", "gyro_x", "gyro_y",
                "gyro_z", "accel_x", "accel_y", "accel_z", "mag_x", "mag_y",
                "mag_z", "hour", "minute", "second", "milisecond", "day",
                "month", "year", "gps_fix", "gps_fix_quality", "latitude",
                "longitude", "speed", "angle", "gps_altitude",
                "gps_num_satellites", "photos_taken", "timestamp"
            ],
            writeFormat="< H",
            writeKeys=["photos_taken"],
            loop=self.loop)
        self.mode = 1  # 1 - idle, 2 - neurals run
        self.n = 0
        self.datadir = os.path.join(os.getcwd(), "data")
        os.makedirs(self.datadir, exist_ok=True)

    async def image(self) -> np.ndarray:
        img = await self.camera.get()
        cv2.imwrite(os.path.join(self.datadir, f"{self.n}_img.png"), img)
        return img

    async def sendAndReceive(self) -> dict:
        self.arduino.put_nowait({"photos_taken": self.n})
        res = await self.arduino.get()
        return res

    # TODO reimplement on stitched map
    async def infer(self, img):
        img = cv2.copyMakeBorder(img, 0, h_roads - h, 0, w_roads - w,
                                 cv2.BORDER_CONSTANT, (0, 0, 0))
        img = np.transpose(img, (2, 0, 1))
        img_roads = np.zeros((35, 3, 256, 256))
        i = 0
        for y in range(0, h_roads, 256):
            for x in range(0, w_roads, 256):
                img_roads[i] = img[:, y:y + 256, x:x + 256]
                i += 1

        result = np.zeros((35, 1, 256, 256))
        for i in range(0, 35, 5):
            self.roads.async_infer(img_roads[i:i + 5], i // 5)
        for i in range(0, 35, 5):
            res = list(self.roads.wait_request(i // 5).values())[0]
            res = np.argmax(res, axis=1) * 255
            result[i:i + 5, 0] = res
        return result

    async def main(self):
        img = await self.image()
        self.n += 1
        while True:
            sensor_data, img, roads_result = await asyncio.gather(
                self.sendAndReceive(), self.image(), self.infer(img))
            roads_result.dump(
                os.path.join(self.datadir, f"{self.n-1}_roads.np"))
            json.dump(
                sensor_data,
                open(os.path.join(self.datadir, f"{self.n}_sensors.json"),
                     "w"))
            self.n += 1


if __name__ == "__main__":
    core = Core()
    try:
        core.loop.run_until_complete(core.main())
    finally:
        core.loop.run_until_complete(core.loop.shutdown_asyncgens())
        core.loop.close()
