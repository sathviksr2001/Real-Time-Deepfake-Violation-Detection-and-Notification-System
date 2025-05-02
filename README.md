
# 🛡 Real-Time Deepfake Violation Detection and Notification System

## 📌 Overview

This project is a real-time face anti-spoofing system that uses a Convolutional Neural Network (CNN) to detect deepfake videos from a webcam feed. If a spoofing attempt or deepfake is detected, the system captures the violating frame, saves it locally, and sends an email alert to notify administrators.

It is inspired by traffic signal surveillance systems, where violations are automatically recorded and reported.

## 🗂 Features

- 🎥 Real-time webcam monitoring
- 🧠 Deepfake detection using a trained CNN model
- 📨 Automatic email notification upon detection
- 🖼 Frame capture and saving of spoofing attempts
- 🧾 Modular code structure for scalability
- 🧪 Trained on the [SDFVD dataset](https://doi.org/10.6084/m9.figshare.28881632)

## 📂 Project Structure

```
Deepfake_Violation_Detection/
├── data_preprocessing/
│   └── extract_frames.py          # Extracts frames from SDFVD videos
├── model_training/
│   └── train_cnn_model.py        # Trains CNN model using real/fake frames
├── realtime_detection/
│   └── detect_and_notify.py      # Real-time webcam deepfake detection
├── notifier/
│   └── send_email.py             # Email alert script
├── models/
│   └── deepfake_cnn_model.h5     # Trained CNN model (saved after training)
├── frames/
│   ├── real/                     # Extracted real frames
│   └── fake/                     # Extracted fake frames
├── violations/
│   └── [timestamp].jpg           # Frames saved on detection
├── README.md
```

## 🧾 Dataset - SDFVD

- **Name**: Small-scale Deepfake Video Dataset (SDFVD)
- **Download**: [https://doi.org/10.6084/m9.figshare.28881632](https://doi.org/10.6084/m9.figshare.28881632)
- **Structure Required**:
  ```
  sdfvd/
  ├── real/
  │   └── *.mp4
  └── fake/
      └── *.mp4
  ```

## ⚙️ Requirements

```bash
pip install tensorflow opencv-python numpy
```

Optional (for sending email alerts):

```bash
pip install secure-smtplib
```

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/deepfake-violation-detection.git
cd deepfake-violation-detection
```

### 2. Download and Prepare the Dataset

- Download the [SDFVD dataset](https://doi.org/10.6084/m9.figshare.28881632)
- Extract into `sdfvd/real/` and `sdfvd/fake/` folders

### 3. Extract Frames

```bash
python data_preprocessing/extract_frames.py
```

### 4. Train the Model

```bash
python model_training/train_cnn_model.py
```

The trained model will be saved in `models/deepfake_cnn_model.h5`

### 5. Configure Email Alerts

In `notifier/send_email.py`, configure:

```python
sender_email = "your_email@gmail.com"
receiver_email = "target_email@gmail.com"
password = "your_app_password"
```

> Use App Passwords or OAuth2 for secure access (for Gmail).

## 🚀 Run the System

Start real-time detection:

```bash
python realtime_detection/detect_and_notify.py
```

- 📷 Captures frames from webcam
- 🔍 Classifies using CNN
- 📩 Sends email and saves frame if spoofing is detected

## 🔒 Email Notification Example

Subject: `Violation Detected - Deepfake Alert`

Message:
```
A spoofing attempt was detected at 2024-05-02 14:30:00.
Screenshot saved to: violations/fake_20240502_143000.jpg
```

## 🧠 Model Details

- **Architecture**: Simple CNN with Conv → MaxPooling → Dense
- **Input**: 64x64 RGB frames
- **Optimizer**: Adam
- **Loss**: Binary Crossentropy
- **Training Data**: Real vs Fake frames from SDFVD

## 🧪 Sample Output

![Sample Output](violations/sample_violation.jpg)

## 🔐 License

MIT License © 2025  
Author: [Your Name]

## 🙋 FAQ

**Q1: Can I use a different dataset?**  
Yes, but ensure it's structured into real/fake and frames can be extracted.

**Q2: Can I run it without email alerts?**  
Yes, you can comment out the `send_email()` line in `detect_and_notify.py`.

## ✨ Contributions

Feel free to fork and enhance this system – e.g., integrating YOLO for face tracking, multi-class classification, or mobile deployment.
