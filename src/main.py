import cv2
import time
from ultralytics import YOLO
from tracker import update_tracker
from utils import draw_tracks

# Load YOLO model
model = YOLO("yolov8n.pt")

# Load video
cap = cv2.VideoCapture("input/input.mp4")

if not cap.isOpened():
    print("❌ Error: Cannot open video")
    exit()

# Output video setup
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("output/output.mp4", fourcc, 30,
                      (int(cap.get(3)), int(cap.get(4))))

frame_count = 0
prev_time = time.time()


while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame_count += 1

    # Skip frames for stability
    if frame_count % 2 != 0:
        continue

    # YOLO detection
    results = model(frame)[0]

    detections = []
    for box in results.boxes.data.tolist():
        x1, y1, x2, y2, score, cls = box

        # Only detect persons (class 0)
        if int(cls) == 0 and score > 0.5:
            detections.append(([x1, y1, x2-x1, y2-y1], float(score), int(cls)))

    # Tracking
    tracks = update_tracker(detections, frame)

    # Draw results
    frame = draw_tracks(frame, tracks)

    # Object count
    cv2.putText(frame, f"Count: {len(tracks)}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2)
    
    # FPS calculation
    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time

    cv2.putText(frame, f"FPS: {int(fps)}",
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2)

    out.write(frame)

cap.release()
out.release()
cv2.destroyAllWindows()