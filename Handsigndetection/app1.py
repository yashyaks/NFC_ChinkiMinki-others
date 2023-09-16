import cv2
import numpy as np
import math
import streamlit as st
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
from datetime import datetime, timedelta
import os

counter = 0
labels = ["A", "B", "C", "D", "Hi", "Y", "W", "Loveu"]

# Load the pre-trained hand detection and classification models
detector = HandDetector(maxHands=1)
classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")

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

# Function to display suitable image based on the label
def display_suitable_image(label):
    image_files = os.listdir("Data")  # Assuming images are in the "Data" directory
    suitable_image = None

    for image_file in image_files:
        if label.lower() in image_file.lower():
            suitable_image = image_file
            break

    if suitable_image:
        img_path = os.path.join("Data", suitable_image)
        img = cv2.imread(img_path)

        if img is not None:
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            st.image(img_rgb, caption=f"Suitable image for {label}")
        else:
            st.write(f"Failed to read the image: {img_path}")
    else:
        st.write(f"No suitable image found for the provided label: {label}")


# Streamlit app
st.title("Sign Language Gesture Classification")

# Initialize video capture
cap = cv2.VideoCapture(0)

# "Capture Image" button to manually capture an image
if st.button("Capture Image"):
    st.write("Capturing image...")
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

        # Display the results
        cv2.rectangle(img, (x - offset, y - offset - 50), (x - offset + 90, y - offset - 50 + 50), (255, 0, 255), cv2.FILLED)
        cv2.putText(img, labels[index], (x, y - 26), cv2.FONT_HERSHEY_COMPLEX, 1.7, (255, 255, 255), 2)
        cv2.rectangle(img, (x - offset, y - offset), (x + w + offset, y + h + offset), (255, 0, 255), 4)

        # Display the image with annotations
        st.image(img, channels="BGR", caption="Hand Gesture Classification")
    else:
        st.write("No hands detected.")

# Input label for suitable image
label_input = st.text_input("Enter a label to display a suitable image:", "A")

# Display suitable image based on input label
if label_input.upper() in labels:
    display_suitable_image(label_input.upper())
else:
    st.write("No suitable image found for the provided label.")

# Stop the webcam if the user closes the Streamlit app
if not st.button("Stop Webcam"):
    cap.release()
    cv2.destroyAllWindows()
