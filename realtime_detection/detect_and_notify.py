import cv2
import tensorflow as tf
import numpy as np
import os
import datetime
from notifier.send_email import send_alert_email

# Load the trained model
model = tf.keras.models.load_model("../models/deepfake_detection_model.h5")

# Start webcam
cap = cv2.VideoCapture(0)

# Directory to save violations
os.makedirs("../violations", exist_ok=True)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    resized = cv2.resize(frame, (64, 64))
    normalized = resized / 255.0
    input_data = np.expand_dims(normalized, axis=0)

    # Predict
    pred = model.predict(input_data)[0][0]

    if pred > 0.5:
        print("FAKE detected!")
        filename = f"../violations/fake_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        cv2.imwrite(filename, frame)
        send_alert_email(filename)

    # Display video feed
    cv2.imshow('Deepfake Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
