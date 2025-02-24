import cv2
import threading
import numpy as np
from retinaface import RetinaFace

# Define camera sources
CAMERA_SOURCES = {
    "camera1": "http://10.24.95.58:4747/video",
    "camera2": "http://10.24.95.54:4747/video",
    "camera3": "http://10.24.93.175:4747/video",
    "camera4": "http://10.24.94.21:4747/video"
}

frames = {name: None for name in CAMERA_SOURCES}
lock = threading.Lock()  # Lock to prevent race conditions

def detect_faces(frame):
    """Run RetinaFace model on the frame to detect faces."""
    if frame is None or frame.size == 0:
        print("[ERROR] Empty frame received in detect_faces()")
        return None

    faces = RetinaFace.detect_faces(frame)
    
    if isinstance(faces, dict) and faces:  # Check if detection was successful
        for _, face in faces.items():
            x1, y1, x2, y2 = face["facial_area"]
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Draw bounding box
    else:
        print("[INFO] No faces detected in the frame.")

    return frame

def capture_and_process_camera(camera_name, url):
    """Capture video and run RetinaFace detection in a separate thread."""
    cap = cv2.VideoCapture(url)
    
    if not cap.isOpened():
        print(f"[ERROR] Unable to open camera: {camera_name}")
        return

    while True:
        ret, frame = cap.read()
        
        if not ret or frame is None:
            print(f"[ERROR] Failed to grab frame from {camera_name}")
            break

        print(f"[INFO] Captured frame from {camera_name}")

        # Perform face detection
        processed_frame = detect_faces(frame)

        if processed_frame is not None:
            with lock:
                frames[camera_name] = processed_frame.copy()  # Copy the frame to prevent corruption

    cap.release()

# Start camera threads
threads = []
for name, url in CAMERA_SOURCES.items():
    thread = threading.Thread(target=capture_and_process_camera, args=(name, url), daemon=True)
    thread.start()
    threads.append(thread)

# Display video streams
while True:
    with lock:
        for name, frame in frames.items():
            if frame is not None:
                cv2.imshow(f"Live Stream - {name}", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
