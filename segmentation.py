import cv2


def main():
    shape = (416, 608)
    model = cv2.dnn.readNet(
        "segmentation/saved_model.xml", "segmentation/saved_model.bin"
    )
    model.setPreferableTarget(cv2.dnn.DNN_TARGET_MYRIAD)
    img = cv2.imread("test.jpg")
    img = cv2.resize(img, shape)
    blob = cv2.dnn.blobFromImage(img)
    model.setInput(blob)
    res = model.forward()
    print(res)


if __name__ == "__main__":
    main()