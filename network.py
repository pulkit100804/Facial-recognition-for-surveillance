#this python code is final for creating a live streaming of two or more camera

import cv2
CAMERA_SOURCES = {
    "camera1": "http://10.24.95.58:4747/video",        
    "camera2": "http://10.24.95.54:4747/video",  
    "camera3": "http://10.24.93.175:4747/video",
    "camera4": "http://10.24.94.21:4747/video"
}

video_captures = {name: cv2.VideoCapture(src) for name, src in CAMERA_SOURCES.items()}
current_camera = "camera1"  # Default camera

while True:
    success, frame = video_captures[current_camera].read()
    if not success:
        print(f"Error: Unable to access {current_camera}")
        break
    cv2.imshow("Live Stream - Press '1' or '2' or '3' to Switch", frame)
    key = cv2.waitKey(1) & 0xFF

    # Switch cameras on key press
    if key == ord('1'):
        current_camera = "camera1"
        print("Switched to Camera 1")
    elif key == ord('2'):
        current_camera = "camera2"
        print("Switched to Camera 2")
    elif key == ord('3'):
        current_camera = "camera3"
        print("Switched to Camera 3")
    elif key == ord('4'):
        current_camera = "camera4"
        print("Switched to Camera 4")    
    elif key == ord('q'):  
        break

for cap in video_captures.values():
    cap.release()
cv2.destroyAllWindows()
