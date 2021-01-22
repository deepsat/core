!source setupvars.sh
import numpy as np
from openvino.inference_engine import IECore, IENetwork
from models import IEModel
import os
import cv2

device = "CPU"

def main():
    ie = IECore()
    if device == "MYRIAD":
        myriad_config = {"VPU_HW_STAGES_OPTIMIZATION": "YES"}
        ie.set_config(myriad_config, "MYRIAD")

    roads = IEModel("models/roads.xml", "models/roads.bin", ie, device, 1)
    img = cv2.imread("frag.png")
    res = roads.infer(img)
    cv2.imwrite(res, "res.png")

if __name__ == "__main__":
    main()