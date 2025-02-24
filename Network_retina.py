import cv2
import numpy as np
from retinaface import RetinaFace

# Define multiple camera sources (Update these)q
CAMERA_SOURCES = {
    "camera1": "http://10.24.95.54:4747/video",  # DroidCam 1 (Update IP)
    ##"camera2": "http://192.168.1.104:4747/video",  # DroidCam 2 (Update IP)
}

# Open video captures for both cameras
video_captures = {name: cv2.VideoCapture(src) for name, src in CAMERA_SOURCES.items()}
current_camera = "camera1"  # Default camera

while True:
    # Read the current camera feed
    success, frame = video_captures[current_camera].read()
    if not success:
        print(f"Error: Unable to access {current_camera}")
        break

    # Face detection using RetinaFace
    faces = RetinaFace.detect_faces(frame)
    
    if isinstance(faces, dict):  # If faces are detected
        for face_id, face in faces.items():
            x1, y1, x2, y2 = face["facial_area"]
            
            # Draw bounding box around the detected face
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, "Face", (x1, y1 - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Show the live feed
    cv2.imshow("Live Stream - Press '1' or '2' to Switch", frame)

    # Wait for key press (1ms delay)
    key = cv2.waitKey(1) & 0xFF

    # Switch cameras on key press
    if key == ord('1'):
        current_camera = "camera1"
        print("Switched to Camera 1")
    elif key == ord('2'):
        current_camera = "camera2"
        print("Switched to Camera 2")
    elif key == ord('q'):  # Press 'q' to exit
        break

# Release resources
for cap in video_captures.values():
    cap.release()
cv2.destroyAllWindows()
