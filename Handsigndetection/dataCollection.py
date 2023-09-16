import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time

counter = 0
cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=2)
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)

    offset = 20
    imgSize = 300

    folder = "Data/Eat"
    if hands:
        hand = hands[0]
        x,y,w,h = hand['bbox']

        imgWhite = np.ones((imgSize,imgSize,3),np.uint8)*255
        imgCrop = img[y-offset:y+h+offset,x-offset:x+w+offset]

        imgCropShape = imgCrop.shape


        aspectRatio = h/w

        if aspectRatio > 1:
            k = imgSize/h
            wcal = math.ceil(k*w)
            imgResize = cv2.resize(imgCrop,(wcal,imgSize))
            imgResizeShape = imgResize.shape
            wGap = math.ceil((300-wcal)/2)
            imgWhite[:, wGap:wcal+wGap] = imgResize
        else:
            k = imgSize/w
            hcal = math.ceil(k*h)
            imgResize = cv2.resize(imgCrop,(imgSize,hcal))
            imgResizeShape = imgResize.shape
            hGap = math.ceil((300-hcal)/2)
            imgWhite[ hGap:hcal+hGap , :] = imgResize    


        cv2.imshow('ImageCrop',imgCrop)
        cv2.imshow('ImageWhite',imgWhite)

    cv2.imshow('image',img)
    key = cv2.waitKey(1)
    if key ==ord('s'):
        counter  += 1
        cv2.imwrite(f'{folder}/Image_{time.time()}.jpg',imgWhite)
        print(counter)
 