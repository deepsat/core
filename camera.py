from picamera import PiCamera
from picamera.array import PiRGBArray
import cv2
from utils import setInterval
import time
import numpy as np
from datetime import datetime

RES = (2592, 1952)


class Camera:
    def start(self):
        self.camera = PiCamera(resolution=RES, framerate=2)
        time.sleep(2)
        self.raw = PiRGBArray(self.camera, size=RES)
        for frame in self.camera.capture_continuous(self.raw, format="bgr", use_video_port=True):
            image = frame.array
            filename = f"output/{datetime.now().strftime('%H%M%S%f')[:-3]}.png"
            print(filename)
            cv2.imwrite(filename, image)
            self.raw.truncate(0)

if __name__ == "__main__":
    camera = Camera()
    camera.start()


# TODO continuous stream and openCV snapping from there
# TODO framerate 1 FPS