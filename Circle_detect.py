import cv2
import numpy as np

# Load the image from file
img = cv2.imread("can.jpg")

# Create a copy of the original image to draw the result on
output = img.copy()

# Convert the image from BGR color space to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise and smooth the image
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Use Hough Circle Transform to detect circles in the blurred image
circle = cv2.HoughCircles(
    blur,
    cv2.HOUGH_GRADIENT,
    dp=1,
    minDist=20,
    param1=100,
    param2=150,
    minRadius=0,
    maxRadius=0
)

# Check if at least one circle was detected
if circle is not None:
    # Round the detected circle parameters and convert them to integers
    circle = np.round(circle[0, :]).astype("int")

    # Loop through each detected circle
    for (x, y, r) in circle:
        # Draw the outer boundary of the detected circle in green
        cv2.circle(output, (x, y), r, (0, 244, 0), 2)

        # Draw the center point of the circle in red
        cv2.circle(output, (x, y), 1, (0, 0, 255), -1)

# Display the output image with detected circles
cv2.imshow("detect circle", output)

# Wait for a key press before closing the window
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()
