from rtcbot import CVCamera
import cv2
import asyncio


async def main():
    w, h = 1600, 1200
    camera = CVCamera(w, h, fps=7)
    img = await camera.get()
    cv2.imwrite(f"test_{w}x{h}.jpg", img)


asyncio.run(main())