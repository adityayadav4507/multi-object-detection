from deep_sort_realtime.deepsort_tracker import DeepSort

# Initialize tracker
tracker = DeepSort(max_age=60,n_init=3)

def update_tracker(detections, frame): # detection come from the YOLO
    return tracker.update_tracks(detections, frame=frame)