import cv2
import os
from tqdm import tqdm

# --- CONFIG ---
video_path = "video.mp4" # Your video
label_list = [...]  # Your 5000-entry list of 'truth', 'false', or 'neutral'
output_dir = "dataset/images"
class_names = ["truth", "false", "neutral"]

# --- Create folders ---
for class_name in class_names:
    os.makedirs(os.path.join(output_dir, class_name), exist_ok=True)

# --- Load video ---
cap = cv2.VideoCapture(video_path)
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

assert len(label_list) == frame_count, "⚠️ Number of labels does not match number of frames!"

frame_idx = 0

# --- Extract and save frames ---
for label in tqdm(label_list, desc="Processing frames"):
    success, frame = cap.read()
    if not success:
        break

    class_dir = os.path.join(output_dir, label)
    filename = f"frame_{frame_idx:05d}.jpg"
    cv2.imwrite(os.path.join(class_dir, filename), frame)
    frame_idx += 1

cap.release()
print("✅ All frames extracted and sorted into class folders.")