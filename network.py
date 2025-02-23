#this python code is final for creating a live streaming of two or more camera

import cv2

# Define multiple camera sources (Update these)
CAMERA_SOURCES = {
    "camera1": "http://192.168.1.108:4747/video",  # DroidCam 1 (Update IP)
    "camera2": "http://192.168.1.104:4747/video",  # DroidCam 2 (Update IP)
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
