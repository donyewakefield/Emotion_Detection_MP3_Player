import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras


# Function that handles face detection and returns last predicted emotion
def capture_expr():
    # Load the model architecture
    with open('model/model_architecture2.json', 'r') as json_file:
        loaded_model_json = json_file.read()
    model = keras.models.model_from_json(loaded_model_json)
    # Load the model weights from HDF5 file
    model.load_weights('model/model_weights2.h5')

    # Initialize facial detection system
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Capture user face
    video_capture = cv2.VideoCapture(0)  # Change the parameter to the appropriate camera index if necessary

    while True:
        # Store as a image frame 
        ret, frame = video_capture.read()
        # Convert from color to gray scale image frame
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            # Focus in on the actual face of the whole frame
            face_img = gray[y:y+h, x:x+w]
            # Resize the facial image to 48x48 pixels
            resized_face = cv2.resize(face_img, (48, 48))
            # Normalize the facial image
            normalized_face = resized_face / 255.0  
            # Reshape the facial image so that it fits in our model
            reshaped_face = np.reshape(normalized_face, (1, 48, 48, 1))

            # Apply the emotion classification model to predict the facial image emotion
            dict = {0:'angry', 1:'happy', 2:'sad', 3:'neutral'}
            emotion_probs = model.predict(reshaped_face)
            # Take the highest probability from the vector 
            emotion_label = np.argmax(emotion_probs)
            # Obtain the actual string label associated with that probability
            emotion_label = dict[emotion_label]

            # Draw bounding box and display emotion label on the frame
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, emotion_label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        cv2.imshow('Facial Expression Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
            break

    video_capture.release()
    cv2.destroyAllWindows()
    return emotion_label




