# Multi-Object Detection and Tracking

## 📌 Overview

This project implements a computer vision pipeline for detecting and tracking multiple objects (players) in sports footage. It assigns persistent IDs to each subject across frames and handles real-world challenges like occlusion and motion.

---

## 🧠 Tech Stack

* YOLOv8 (Ultralytics) → Object Detection
* DeepSORT → Multi-object Tracking
* OpenCV → Video Processing

---

## 🚀 Features

* Multi-object detection (players)
* Persistent ID tracking
* Bounding box visualization
* Trajectory tracking (movement paths)
* Object count per frame
* FPS display

---

## ⚙️ Setup Instructions

### Option 1: Using venv

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

### Option 2: Using Conda

conda create -n yolo_env python=3.10

conda activate yolo_env

pip install -r requirements.txt

---

## ▶️ Run the Project

cd src

python main.py

---


## 📁 Project Structure

```bash
multi-object-tracking/
├── input/                # Input video
├── output/               # Processed output video
├── src/                  # Core source code
│   ├── main.py           # Pipeline execution
│   ├── utils.py          # Visualization utilities
│   └── tracker.py        # Tracking logic
├── requirements.txt      # Dependencies
├── README.md             # Project documentation
└── report.pdf            # Technical report

```

## 📊 Assumptions

* Only "person" class is tracked
* Video is continuous (no scene cuts)

---

## ⚠️ Limitations

* ID switching in heavy occlusion
* Reduced accuracy in motion blur
* No team classification

---

## 🔮 Future Improvements

* Use ByteTrack for better tracking
* Team classification (jersey color)

* Heatmap visualization
* Speed estimation

---

## 🔗 Video Source
https://www.pexels.com/video/exciting-soccer-team-warm-up-session-in-stadium-34452654/

## Demo

<p align="center">
  <img src="https://github.com/user-attachments/assets/9424622d-e6b8-43b8-8d4d-471c9e8f754e" width="500"/>
</p>


