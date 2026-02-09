#Import Flask and jsonify modules to create the API and return JSON responses
from flask import Flask, jsonify, Response
import time
import cv2
from threading

# Initialize Flask application instance named 'api'
api = Flask(__name__)
# Define the root endpoint '/' that provides a welcome message and lists available API endpoints
@api.route('/', methods=['GET'])
def home():
  """
  Home route: Returns a welcome comment and lists all available control endpoints.
  Method: GET
  """
  return jsonify({
        "comment": "Robot Control API home page",
        "available_endpoints": [
        "/forward",
        "/backward",
        "/left",
        "/right",
        "/stop",
        "/start"
    ]
  })
# Define endpoint to handle the forward movement command
@api.route('/forward', methods=['GET'])
def forward():
  """
  Forward route: Instructs the robot to move forward.
  Method: GET
  """
  return jsonify({"comment": "moving forward"})
# Define endpoint to handle the backward movement command
@api.route('/backward', methods=['GET'])
def backward():
  """
  Backward route: Instructs the robot to move backward.
  Method: GET
  """
  return jsonify({"comment": "moving backward"})
# Define endpoint to handle the left turn command
@api.route('/left', methods=['GET'])
def left():
  """
  Left route: Instructs the robot to turn left.
  Method: GET
  """
  return jsonify({"comment": "turning left"})
# Define endpoint to handle the right turn command
@api.route('/right', methods=['GET'])
def right():
  """
  Right route: Instructs the robot to turn right.
  Method: GET
  """
  return jsonify({"comment": "turning right"})
# Define endpoint to stop the robot
@api.route('/stop', methods=['GET'])
def stop():
  """
  Stop route: Instructs the robot to stop all movement.
  Method: GET"""
  return jsonify({"comment": "robot stopped"})
# Define endpoint to start the robot
@api.route('/start', methods=['GET'])
def start():
  """
  Start route: Instructs the robot to start operation.
  Method: GET
  """
  return jsonify({"comment": "robot started"})  
cap = cv2.VideoCapture(0)
lock=threading.Lock()
def process_frame(frame):
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  
def gen_raw():
    while True:
      with lock:
        success, frame=cap.read()
      if not success:
        break
      ret, buffer=cv2.imencode('.jpg',frame)
      frame_bytes=buffer.tobytes()
      yield(b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n'+frame_bytes+b'\r\n')
def gen_processed():
  while True:
    with lock:
      success,frame= cap.read()
    if not success:
      break
    processed=process_frame(frane.copy())
    ret, buffer=cv2/imencode('.jpg',processed)
    frame_bytes=buffer.tobytes()
    yield(b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n'+frame_bytes+b'\r\n')
@api.route('/video_processed')
def video_processed():
    return Response(gen_processed(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@api.route('/video_raw')
def video_raw():
    return Response(gen_raw(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# Run the Flask app with debug mode enabled if the script is executed directly
if __name__ == '__main__':
    api.run(host='0.0.0.0',port='5010',debug=True)
