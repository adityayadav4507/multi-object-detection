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

multi-object-tracking/
├── input/input.mp4
├── output/output.mp4
├── src/
      ├──main.py
      ├──utils.py
      └── tracker.py
├── requirements.txt
├── README.md
└── report.pdf

---

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

(Add your YouTube/public video link here)
