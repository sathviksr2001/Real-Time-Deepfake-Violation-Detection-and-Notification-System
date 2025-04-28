import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Paths
frames_dir = "../frames"
model_save_path = "../models/deepfake_detection_model.h5"

# Data generator
datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

train_gen = datagen.flow_from_directory(
    frames_dir,
    target_size=(64, 64),
    batch_size=32,
    class_mode='binary',
    subset='training')

val_gen = datagen.flow_from_directory(
    frames_dir,
    target_size=(64, 64),
    batch_size=32,
    class_mode='binary',
    subset='validation')

# Model
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(64,64,3)),
    MaxPooling2D(2,2),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Training
model.fit(train_gen, epochs=10, validation_data=val_gen)

# Save model
os.makedirs("../models", exist_ok=True)
model.save(model_save_path)
