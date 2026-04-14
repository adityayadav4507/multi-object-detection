import cv2
from collections import defaultdict
# Store trajectories
track_history = defaultdict(list)

def draw_tracks(frame, tracks):
    for track in tracks:
        if not track.is_confirmed():
            continue

        track_id = track.track_id
        l, t, r, b = track.to_ltrb()

        cx = int((l + r) / 2)
        cy = int((t + b) / 2)

        # Store trajectory
        track_history[track_id].append((cx, cy))

        # Limit trajectory length
        if len(track_history[track_id]) > 30:
            track_history[track_id].pop(0)

        # Draw bounding box
        cv2.rectangle(frame, (int(l), int(t)),
                      (int(r), int(b)), (0,255,0), 2)

        # Draw ID
        cv2.putText(frame, f"ID {track_id}",
                    (int(l), int(t)-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, (0,255,0), 2)
        
        # Draw trajectory
        for i in range(1, len(track_history[track_id])):
            cv2.line(frame,
                     track_history[track_id][i - 1],
                     track_history[track_id][i],
                     (255, 0, 0), 2)

    return frame