import cv2
import numpy as np
import time

def capture_and_save_cropped_image(file_path):
    
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    ret, frame = cap.read()

    if not ret:
        print("Error: Could not capture image.")
        cap.release()
        return

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) > 0:
        x, y, w, h = faces[0]

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cropped_face = frame[y:y + h, x:x + w] # crops the area around the anchor boxx..

        cv2.imwrite(file_path, cropped_face)

        cv2.imshow('Original Image with Anchor Box', frame)

        cv2.imshow('Cropped Face', cropped_face)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("No face detected.")

    cap.release()

file_path = f'images/cropped_face1_.jpg'

capture_and_save_cropped_image(file_path)
