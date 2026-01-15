
import cv2
import numpy as np

# Open the moving can video file
cap = cv2.VideoCapture("moving_cir.mp4")

while True:
    # Read one frame from the video
    ret, frame = cap.read()
    if not ret:
        break

    # Copy frame for drawing results
    output = frame.copy()

    # Convert BGR image to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define HSV range for can top
    lower_gray = np.array([0, 0, 40])
    upper_gray = np.array([180, 80, 210])

    # Create mask to keep only gray regions (can top)
    mask = cv2.inRange(hsv, lower_gray, upper_gray)

    # Apply mask to original frame
    gray_only = cv2.bitwise_and(frame, frame, mask=mask)

    # Convert masked image to grayscale
    gray = cv2.cvtColor(gray_only, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise and smooth edges
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Detect circles using Hough Circle Transform
    circles = cv2.HoughCircles(
        blur,
        cv2.HOUGH_GRADIENT,
        dp=1.2,
        minDist=50,
        param1=100,
        param2=100,
        minRadius=140,
        maxRadius=160
    )

    # Draw detected circles on the original video
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            cv2.circle(output, (x, y), r, (0, 255, 0), 2)
            cv2.circle(output, (x, y), 2, (0, 0, 255), -1)

    # Display the result
    cv2.imshow("Can Top Detection", output)

# Release video resources and close windows
cap.release()
cv2.destroyAllWindows()
