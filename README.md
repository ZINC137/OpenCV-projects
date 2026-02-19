# 🚁 Drone Vision System using OpenCV

This project implements classical computer vision techniques for aerial robotics applications.

It includes:

• 🌿 Yellow Leaf Detection (Crop Health Monitoring)  
• 🎯 Real-Time ArUco Marker Detection with Pose Estimation  

---

## 🌿 1. Yellow Leaf Detection

Detects infected (yellow) leaves in both static images and real-time webcam feed.

### Image-Based Detection:
- Load image using `cv2.imread()`
- Convert from BGR to HSV color space
- Apply yellow threshold using `cv2.inRange()`
- Remove noise using morphological operations
- Detect contours
- Draw bounding boxes around infected regions

### Live Webcam Detection:
- Capture frames using `cv2.VideoCapture()`
- Convert each frame to HSV
- Apply yellow threshold in real-time
- Clean mask using morphological operations
- Detect contours frame-by-frame
- Display bounding boxes on live video feed

## 🎯 2. ArUco Marker Detection

Detects ArUco markers in real-time using webcam feed.

### Features:
- Marker ID detection
- Bounding box visualization
- 3D pose estimation
- Coordinate axis overlay

---

## 🛠️ Tech Stack

- Python
- OpenCV (opencv-contrib-python)
- NumPy
- HSV Color Segmentation
- Contour Detection
- Pose Estimation

---

## 🚀 Applications

- Precision Agriculture
- Drone Navigation
- Autonomous Landing
- Visual Localization

---

## 👤 Author

Smruti Ranjan Ghosh  
Aerial Robotics Vision Project
