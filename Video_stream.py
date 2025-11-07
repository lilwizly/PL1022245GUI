import cv2

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
if not cap.isOpened():
  print("Not open")
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
