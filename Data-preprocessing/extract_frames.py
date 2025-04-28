import cv2
import os

def extract_frames(video_path, save_dir, label):
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_filename = os.path.join(save_dir, f"{label}_{os.path.basename(video_path)[:-4]}_frame{frame_count}.jpg")
        cv2.imwrite(frame_filename, frame)
        frame_count += 1
    cap.release()

def process_dataset(dataset_path, output_path):
    real_path = os.path.join(dataset_path, 'real')
    fake_path = os.path.join(dataset_path, 'fake')
    os.makedirs(output_path, exist_ok=True)
    for vid in os.listdir(real_path):
        extract_frames(os.path.join(real_path, vid), output_path, label='real')
    for vid in os.listdir(fake_path):
        extract_frames(os.path.join(fake_path, vid), output_path, label='fake')

if __name__ == "__main__":
    dataset_path = "../SDFVD"  # <-- Your downloaded dataset path
    output_path = "../frames"
    process_dataset(dataset_path, output_path)
