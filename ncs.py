import numpy as np
from openvino.inference_engine import IECore, IENetwork
from models import IEModel
import os
import cv2
from time import time

device = "MYRIAD"

def main():
    ie = IECore()

    roads = IEModel("models/roads.xml", "models/roads.bin", ie, device, 1) 
    objects = IEModel("models/objects.xml", "models/objects.bin", ie, device, 1)

    img = np.expand_dims(np.transpose(cv2.imread("frag.png"), (2,0,1)), 0)
    img416 = np.zeros((1,3,416,416))
    img416[:,:,:256,:256] = img
    print("Starting inference")
    start = time()
    res_roads = roads.infer(img)
    res_objects = objects.infer(img416)
    end = time()
    print(f"Finished inference. Took {end - start} seconds.")

    print(res_roads)
    print(res_objects)
    
    
if __name__ == "__main__":
    main()
