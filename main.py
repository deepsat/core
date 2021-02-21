import asyncio
from rtcbot import PiCamera, CVCamera
from rtcbot.arduino import SerialConnection
import numpy as np
import cv2
from datetime import datetime

loop = asyncio.get_event_loop()

camera = CVCamera(width=4160, height=3120, fps=7, loop=loop)
# camera = PiCamera(width=1296, height=976, fps=30, loop=loop)
# arduino = SerialConnection(
#     url="/dev/ttyAMA1",
#     writeFormat="<HB",
#     writeKeys=["value1", "value2"],
#     readFormat="<BH",
#     readKeys=["value1", "value2"],
#     loop=loop,
# )


async def image():
    img = await camera.get()
    cv2.imwrite(f"camera/{datetime.now()}.png", img)
    return img


async def send():
    ...


async def receive():
    ...


async def main():
    while True:
        a, b, c = await asyncio.gather(image(), send(), receive())
        print(datetime.now(), a, b, c)
        await asyncio.sleep(0.5)

if __name__=="__main__":
    asyncio.ensure_future(main())
    loop.run_forever()