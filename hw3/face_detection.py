import numpy as np
import cv2
import paho.mqtt.client as mqtt

# Create a new client instance and connect to the local broker.
client = mqtt.Client()
client.connect("172.18.0.2")

# Use the web camera to capture frame.
cap = cv2.VideoCapture(1)

while(True):
    # Capture frame-by-frame.
    ret, frame = cap.read()
    # Throw out the color information and get the gray frame.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Face detection.
    face_cascade = cv2.CascadeClassifier('/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml')

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:

        face = frame[y:y+h, x:x+w]

        rc, jpg=cv2.imencode('.png', face)
	
        msg = jpg.tobytes()

        client.publish("faces_detected", payload=msg)

        cv2.waitKey(1)
        break
        
cap.release()
cv2.destroyAllWindows()
