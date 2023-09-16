import cv2
import numpy as np
from django.shortcuts import render
from django.http import StreamingHttpResponse
from django.views.decorators import gzip
import mediapipe as mp
from tensorflow import keras
from channels.generic.websocket import AsyncWebsocketConsumer
import asyncio
import json
from gtts import gTTS
from playsound import playsound
import subprocess
from django.http import JsonResponse
# from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
# from transformers import TFMBartForConditionalGeneration
import time
global sequence
sequence = []
global sentence
sentence = []
# model_translate = TFMBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-one-to-many-mmt")
# tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-one-to-many-mmt", src_lang="en_XX")


# def text_to_speech(request):
#     global sentence
#     text = ' '.join(sentence)
#     ttsForSentence(text)

#     return JsonResponse({'status': 'Audio generated'})

# def ttsForSentence(text):
#     tts = gTTS(text)
#     tts.save("home/output.mp3")


def update_sentences(request):
    # global sentence  # Declare sentence as a global variable
    # Get the list of sentences as a string
    sentence_text = ' '.join(sentence)
    # Clear the sentence list
    # sentence = []
    return JsonResponse({'sentences': sentence_text})


def text_to_speech(request):
    text = ' '.join(sentence)
    tts = gTTS(text)
    tts.save("home/output.mp3")
    playsound("home/output.mp3")
    return JsonResponse({'status': 'Audio generated'})
    

mp_holistic = mp.solutions.holistic
mp_drawings = mp.solutions.drawing_utils

websocket_url = "ws://http://127.0.0.1:8000/live_feed" 
# Load your model and define actions and colors as in your code
model = keras.models.load_model('home/action.h5')
# model = keras.models.load_model('home/keras_model.h5')
# actions = np.array(['A', 'B', 'C', 'D', 'W', 'Y', 'Z', 'Hi', 'IloveYou'])
actions = np.array(['Hello', 'Thanks', 'IloveYou'])
colors = [(0, 255, 0), (0, 255, 0), (255, 0, 0)]



# Define the sequence and sentence variables as global


def extract_keypoints(results):
    pose = np.array([[res.x, res.y, res.z, res.visibility] for res in results.pose_landmarks.landmark]).flatten() if results.pose_landmarks else np.zeros(33*4)
    face = np.array([[res.x, res.y, res.z] for res in results.face_landmarks.landmark]).flatten() if results.face_landmarks else np.zeros(468*3)
    lh = np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(21*3)
    rh = np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).flatten() if results.right_hand_landmarks else np.zeros(21*3)
    return np.concatenate([pose, face, lh, rh])

def mediapipe_detection(image, model):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # COLOR CONVERSION BGR 2 RGB
    image.flags.writeable = False                  # Image is no longer writeable
    results = model.process(image)                 # Make prediction
    image.flags.writeable = True                   # Image is now writeable 
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # COLOR COVERSION RGB 2 BGR
    return image, results

def draw_landmarks(image, results):
    mp_drawings.draw_landmarks(image, results.face_landmarks, mp_holistic.FACEMESH_TESSELATION) # Draw face connections
    mp_drawings.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS) # Draw pose connections
    mp_drawings.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS) # Draw left hand connections
    mp_drawings.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

def draw_styled_landmarks(image, results):
    # Draw face connections
    mp_drawings.draw_landmarks(image, results.face_landmarks, mp_holistic.FACEMESH_TESSELATION, 
                             mp_drawings.DrawingSpec(color=(80,110,10), thickness=1, circle_radius=1), 
                             mp_drawings.DrawingSpec(color=(80,256,121), thickness=1, circle_radius=1)
                             ) 
    # Draw pose connections
    mp_drawings.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                             mp_drawings.DrawingSpec(color=(80,22,10), thickness=2, circle_radius=4), 
                             mp_drawings.DrawingSpec(color=(80,44,121), thickness=2, circle_radius=2)
                             ) 
    # Draw left hand connections
    mp_drawings.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                             mp_drawings.DrawingSpec(color=(121,22,76), thickness=2, circle_radius=4), 
                             mp_drawings.DrawingSpec(color=(121,44,250), thickness=2, circle_radius=2)
                             ) 
    # Draw right hand connections  
    mp_drawings.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                             mp_drawings.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=4), 
                             mp_drawings.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)
                             )

threshold = 0.8
sample_rate = 0.1


def gen_frames():
    cap = cv2.VideoCapture(0)
    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            image, results = mediapipe_detection(frame, holistic)
            keypoints = extract_keypoints(results)
            global sequence  # Declare sequence as a global variable
            sequence.append(keypoints)
            sequence = sequence[-30:]

            if len(sequence) == 30:
                res = model.predict(np.expand_dims(sequence, axis=0))[0]

                if res[np.argmax(res)] > threshold:
                    global sentence  # Declare sentence as a global variable
                    if len(sentence) > 0:
                        if actions[np.argmax(res)] != sentence[-1]:
                            sentence.append(actions[np.argmax(res)])
                            # Announce the newly predicted text
                            # text_to_speech(actions[np.argmax(res)])
                    else:
                        sentence.append(actions[np.argmax(res)])
                        # Announce the newly predicted text
                        # text_to_speech(actions[np.argmax(res)])

                if len(sentence) > 5:
                    sentence = sentence[-5:]

            # Draw MediaPipe landmarks and connections on the image
            draw_styled_landmarks(image, results)

            # Render the sentence on the image
            sentence_text = ' '.join(sentence)
            cv2.putText(image, sentence_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            ret, buffer = cv2.imencode('.jpg', cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
            if not ret:
                continue
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            print(sentence_text)


            
def index(request):
    return render(request, 'index.html')

@gzip.gzip_page
def live_feed(request):
    return StreamingHttpResponse(gen_frames(), content_type="multipart/x-mixed-replace;boundary=frame")

class PredictTextConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

#     async def disconnect(self, close_code):
#         pass

#     async def send_predicted_text(self, text):
#         await self.send(text)

async def process_frames_and_send_text():
    while True:
        await asyncio.sleep(1)  # Adjust the sleep duration as needed
        print('aaya')
        # if len(sentence) > 0:
        print('aa rha hai')
        sentence_text = ' '.join(sentence) # Get the latest predicted text
        text_json = json.dumps({"message": sentence_text})

            # Broadcast the predicted text to all connected WebSocket clients
        await PredictTextConsumer.broadcast(text_json)

# Start the background task to process frames and send text
# async def send_predicted_text(self, text):
#     await self.send(text)
#     text_to_speech(text)
def new_data(request):
    cap = cv2.VideoCapture(0)
    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    
    # NEW LOOP
    # Loop through actions
    
        # Loop through sequences aka videos
        for sequence in range(15):
            # Loop through video length aka sequence length
            for frame_num in range(30):

                    # Read feed
                ret, frame = cap.read()

                    # Make detections
                image, results = mediapipe_detection(frame, holistic)
    #                 print(results)

                    # Draw landmarks
                draw_styled_landmarks(image, results)
                    
                    # NEW Apply wait logic
                if frame_num == 0: 
                    cv2.putText(image, 'STARTING COLLECTION', (120,200), 
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255, 0), 4, cv2.LINE_AA)
                    cv2.putText(image, 'Collecting frames for {} Video Number {}'.format(action, sequence), (15,12), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                        # Show to screen
                    cv2.imshow('OpenCV Feed', image)
                    cv2.waitKey(2000)
                else: 
                    cv2.putText(image, 'Collecting frames for {} Video Number {}'.format(action, sequence), (15,12), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                        # Show to screen
                    cv2.imshow('OpenCV Feed', image)
                    
                    # NEW Export keypoints
                keypoints = extract_keypoints(results)
                # npy_path = os.path.join(DATA_PATH, action, str(sequence), str(frame_num))
                # np.save(npy_path, keypoints)

                    # Break gracefully
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
                        
        cap.release()
        cv2.destroyAllWindows()
# def translate(request):
#     model_inputs = tokenizer(' '.join(sentence), return_tensors="pt")
#     # time.wait(15)
#     generated_tokens = model_translate.generate(
#         **model_inputs,
#         forced_bos_token_id=tokenizer.lang_code_to_id["hi_IN"]
#     )
#     translation = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
#     print(translation)
#     return JsonResponse({'translated':translation})
loop = asyncio.get_event_loop()
loop.create_task(process_frames_and_send_text())