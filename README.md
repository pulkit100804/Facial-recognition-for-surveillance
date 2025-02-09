# 🔍 Real-Time Facial Recognition & Surveillance System

This project is a **real-time facial recognition and multi-camera tracking system** designed for law enforcement. It uses **RetinaFace** for face detection and alignment, **FaceNet/ArcFace** for deep learning-based recognition, and **Firebase Firestore** for database storage. When a suspect is identified, **Firebase Cloud Messaging** sends real-time alerts, and the system maps their movement across multiple cameras.

## 🚀 Features
- 📸 **Face Detection & Alignment:** RetinaFace ensures accurate face localization.
- 🧠 **Deep Learning Recognition:** FaceNet/ArcFace generates unique facial embeddings.
- ⚡ **Real-Time Alerts:** Firebase Cloud Messaging notifies authorities instantly.
- 🎥 **Multi-Camera Tracking:** Logs camera IDs to track a suspect's movement.
- 📊 **Dashboard Visualization:** Displays travel paths based on camera detections.

## 🛠 Tech Stack
- **Face Detection:** RetinaFace
- **Face Recognition:** FaceNet / ArcFace
- **Database:** Firebase Firestore
- **Backend:** Python, OpenCV, TensorFlow/PyTorch
- **Tracking:** Multi-camera logging with ID mapping
- **Notifications:** Firebase Cloud Messaging

## ⚙️ Installation
```sh
git clone https://github.com/your-repo/facial-recognition-tracking.git
cd facial-recognition-tracking
pip install -r requirements.txt
```

## 📌 Usage
```sh
python main.py
```

## 📷 Multi-Camera Tracking
Every time a face is detected, the system records the **camera ID** in Firebase, creating a movement history that can be visualized on the dashboard.

## 📝 License
This project is licensed under the **MIT License**.
