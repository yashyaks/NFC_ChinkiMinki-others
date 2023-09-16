import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import tensorflow
import numpy as np
import math
import mediapipe as mp


counter = 0
labels = ["A","B","C","D","Hi","Y","W","Loveu"]
cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
Classifier = Classifier("Model/keras_model.h5","Model/labels.txt")
while True:
    success, img = cap.read()
    imgOutput = img.copy()
    hands, img = detector.findHands(img)

    offset = 20
    imgSize = 300

    folder = "Data/C"
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
            prediction ,index = Classifier.getPrediction(imgWhite,draw = False)
            print(prediction,index)
            
        else:
            k = imgSize/w
            hcal = math.ceil(k*h)
            imgResize = cv2.resize(imgCrop,(imgSize,hcal))
            imgResizeShape = imgResize.shape
            hGap = math.ceil((300-hcal)/2)
            imgWhite[ hGap:hcal+hGap , :] = imgResize    
            prediction ,index = Classifier.getPrediction(imgWhite,draw = False)
            print(prediction,index)


        cv2.rectangle(imgOutput,(x-offset,y-offset-50),(x-offset+90,y-offset-50+50),(255,0,255),cv2.FILLED)       
        cv2.putText(imgOutput,labels[index],(x,y-26),cv2.FONT_HERSHEY_COMPLEX,1.7,(255,255,255),2) 
        cv2.rectangle(imgOutput,(x-offset,y-offset),(x+w+offset,y+h+offset),(255,0,255),4)       


        cv2.imshow('ImageCrop',imgCrop)
        cv2.imshow('ImageWhite',imgWhite)

    cv2.imshow('image',imgOutput)
    cv2.waitKey(1)

 