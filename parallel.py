import cv2
import numpy as np

def detect_parallel(frame):
    h, w = frame.shape[:2]
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([140, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    mask = cv2.GaussianBlur(mask, (5,5), 0)
    edges = cv2.Canny(mask, 50, 150)
    contours, _ = cv2.findContours(
        edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    draw = frame.copy()

    if len(contours) >= 2:
        l1 = contours[0].reshape(-1,2)
        l2 = contours[1].reshape(-1,2)

        cv2.polylines(draw, [l1], False, (0,0,255), 2)
        cv2.polylines(draw, [l2], False, (0,255,0), 2)

        n = min(len(l1), len(l2))
        p1 = l1[np.linspace(0, len(l1)-1, n, dtype=int)]
        p2 = l2[np.linspace(0, len(l2)-1, n, dtype=int)]
        center = ((p1 + p2) / 2).astype(int)

        cv2.polylines(draw, [center], False, (255,0,0), 2)

        dx = center[-1][0] - center[0][0]
        if dx > 10:
            direction = "RIGHT"
        elif dx < -10:
            direction = "LEFT"
        else:
            direction = "STRAIGHT"

        cv2.putText(draw, direction, (40,40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)

    return draw
