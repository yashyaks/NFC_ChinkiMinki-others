import cv2
import numpy as np
import math
import streamlit as st
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
from datetime import datetime, timedelta
from gtts import gTTS
import os

counter = 0
labels = ["A", "B", "C", "D", "Hi", "Y", "W", "Loveu"]

# Load the pre-trained hand detection and classification models
detector = HandDetector(maxHands=1)
classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")

# Initialize video capture to None
cap = None

# Function to perform hand gesture classification
def classify_hand_gesture(img_crop):
    img_white = np.ones((img_size, img_size, 3), np.uint8) * 255
    img_crop_shape = img_crop.shape

    aspect_ratio = img_crop_shape[0] / img_crop_shape[1]

    if aspect_ratio > 1:
        k = img_size / img_crop_shape[0]
        w_cal = math.ceil(k * img_crop_shape[1])
        img_resize = cv2.resize(img_crop, (w_cal, img_size))
        img_white[:, (img_size - w_cal) // 2 : (img_size - w_cal) // 2 + w_cal] = img_resize
        prediction, index = classifier.getPrediction(img_white, draw=False)
        return prediction, index
    else:
        k = img_size / img_crop_shape[1]
        h_cal = math.ceil(k * img_crop_shape[0])
        img_resize = cv2.resize(img_crop, (img_size, h_cal))
        img_white[(img_size - h_cal) // 2 : (img_size - h_cal) // 2 + h_cal, :] = img_resize
        prediction, index = classifier.getPrediction(img_white, draw=False)
        return prediction, index

# Function to convert text to speech
def text_to_speech(text, lang='en'):
    tts = gTTS(text, lang=lang)
    tts.save("output.mp3")
    os.system("mpg123 output.mp3")

# Streamlit app
st.title("SignSway")

# Variables for image capture and classification
capture_time = datetime.now()  # Initial capture time
capture_interval = timedelta(seconds=3)  # Image capture interval
last_capture = datetime.now() - capture_interval  # Last captured image time

# Constants for image resizing
offset = 20
img_size = 300

# Function to capture an image and classify the hand gesture
def capture_and_classify():
    global last_capture
    last_capture = datetime.now()

    # Capture image from webcam
    success, img = cap.read()

    # Find hands in the frame
    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']

        img_crop = img[y - offset : y + h + offset, x - offset : x + w + offset]

        # Classify hand gesture
        prediction, index = classify_hand_gesture(img_crop)

        # Convert prediction to speech
        text_to_speech(labels[index])

        # Display the results
        cv2.rectangle(img, (x - offset, y - offset - 50), (x - offset + 90, y - offset - 50 + 50), (255, 0, 255), cv2.FILLED)
        cv2.putText(img, labels[index], (x, y - 26), cv2.FONT_HERSHEY_COMPLEX, 1.7, (255, 255, 255), 2)
        cv2.rectangle(img, (x - offset, y - offset), (x + w + offset, y + h + offset), (255, 0, 255), 4)

        # Display the image with annotations
        st.image(img, channels="BGR", caption="Hand Gesture Classification")

# Start/Stop webcam buttons
if not cap:
    cap = cv2.VideoCapture(0)

# Display the Streamlit app
st.write("## Sign Language Gesture Classification")
st.write("Show your hand in front of the camera to classify the sign language gesture.")

# "Capture Image" button to manually capture an image
if st.button("Capture Image"):
    capture_and_classify()

# Capture images every 3 seconds
if (datetime.now() - last_capture) >= capture_interval:
    capture_and_classify()
    last_capture = datetime.now()

# Button to convert the predicted label to speech
if st.button("Convert to Speech"):
    text_to_speech("This is a test message")  # Replace with the predicted label

# Stop the webcam if the user closes the Streamlit app
if not st.button("Stop Webcam"):
    cap.release()
    cv2.destroyAllWindows()
