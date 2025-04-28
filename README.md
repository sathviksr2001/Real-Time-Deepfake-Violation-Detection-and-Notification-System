# Real-Time Deepfake Violation Detection and Notification System

## Overview

This project is designed to detect deepfake videos in real-time using a webcam feed. If a violation (deepfake content) is detected, the system sends an email notification and saves the detected frame in the **violations/** directory for further review. The deepfake detection is powered by a Convolutional Neural Network (CNN) model trained using the **SDFVD (Small-Scale Deepfake Video Dataset)**.

## Features

- **Real-Time Deepfake Detection**: Detect deepfake content using a webcam feed.
- **Email Alerts**: Sends an email notification when a violation (deepfake) is detected.
- **Frame Saving**: Saves detected deepfake frames in a dedicated folder (`violations/`).
- **CNN Model**: The model is trained on extracted frames from deepfake videos (SDFVD dataset).
- **Minimal Setup**: Easy to set up and run for detecting deepfakes.

## Table of Contents

- [Features](#features)
- [Dataset](#dataset)
- [Requirements](#requirements)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Setup](#setup)
- [Steps to Run](#steps-to-run)
- [License](#license)

## Dataset

This project uses the **SDFVD** (Small-Scale Deepfake Video Dataset) for training the deepfake detection model. The dataset consists of **real** and **fake** video clips, which are used to train the model to distinguish between authentic and manipulated content.

- **Real Videos**: Authentic video clips of people.
- **Fake Videos**: Deepfake video clips of people generated using deepfake algorithms.

> **Note**: You need to download the SDFVD dataset and place it in the correct folder for processing.

- **Dataset Download Link**: [SDFVD Dataset (Figshare)](https://doi.org/10.6084/m9.figshare.28881632)

## Requirements

### Software Dependencies
- Python 3.x
- TensorFlow (for deep learning)
- OpenCV (for video and webcam processing)
- NumPy (for numerical operations)
- smtplib (for sending email alerts)

### Install Dependencies

Use the following commands to install the required dependencies:

```bash
pip install tensorflow opencv-python numpy
# Project Structure
The project directory structure is organized as follows:

bash
Copy
Edit
Deepfake_Violation_Detection_Project/
├── data_preprocessing/
│   └── extract_frames.py            # Script to extract frames from videos
├── model_training/
│   └── train_cnn_model.py          # Script to train the CNN model
├── realtime_detection/
│   └── detect_and_notify.py        # Script for real-time detection and email notifications
├── notifier/
│   └── send_email.py               # Script for sending email notifications
├── models/
│   └── deepfake_detection_model.h5 # Trained model will be saved here
├── violations/
│   └── fake_20230428_153000.jpg    # Fake frames detected will be saved here
├── frames/
│   ├── real_video_frame0.jpg       # Extracted frames from real videos
│   ├── fake_video_frame1.jpg      # Extracted frames from fake videos
│   └── ...
└── README.md                       # This readme file
