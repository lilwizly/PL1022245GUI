import cv2

cap = cv2.VideoCapture
if not cap.isOpened():
  print("Error:Could not open video stream.")
  exit()
while True:
  ret, frame =cap.read()

  if not ret:
    print("Error: Fao;ed tp retrieve frame.")
    break
  cv2.imshow('Live Stream',frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()
