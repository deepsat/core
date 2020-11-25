import asyncio
from rtcbot import PiCamera
from rtcbot.arduino import SerialConnection
import numpy as np
import cv2
from datetime import datetime

# #	Resolution	Aspect Ratio    Framerates  Video	Image	FoV	    Binning
# 1	1920x1080	16:9            1-30fps	    x	 	        Partial	None
# 2	2592x1952	4:3	            1-15fps	    x	    x	    Full	None
# 3	2592x1952	4:3	            0.1666-1fps	x	    x	    Full	None
# 4	1296x976	4:3	            1-42fps	    x	 	        Full	2x2
# 5	1296x730	16:9	        1-49fps	    x	 	        Full	2x2
# 6	640x480	    4:3	            42.1-60fps	x	 	        Full	4x4
# 7	640x480	    4:3	            60.1-90fps	x	 	        Full	4x4
loop = asyncio.get_event_loop()

camera = PiCamera(width=1296, height=976, fps=30, loop=loop)
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
        await asyncio.sleep(1)


try:
    asyncio.ensure_future(main())
    loop.run_forever()
finally:
    camera.close()