import cv2
import threading

# Define camera sources
CAMERA_SOURCES = {
    "camera1": "http://10.24.95.58:4747/video",        
    "camera2": "http://10.24.95.54:4747/video",  
    "camera3": "http://10.24.93.175:4747/video",
    "camera4": "http://10.24.94.21:4747/video" 
}

frames = {name: None for name in CAMERA_SOURCES}

def capture_camera(camera_name, url):
    """Function to capture video from a camera in a separate thread."""
    cap = cv2.VideoCapture(url)
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            frames[camera_name] = frame  
        else:
            print(f"Error: Unable to access {camera_name}")
            break
    cap.release()
threads = []
for name, url in CAMERA_SOURCES.items():
    thread = threading.Thread(target=capture_camera, args=(name, url), daemon=True)
    thread.start()
    threads.append(thread)

while True:
    for name, frame in frames.items():
        if frame is not None:
            cv2.imshow(f"Live Stream - {name}", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"): 
        break

cv2.destroyAllWindows()
