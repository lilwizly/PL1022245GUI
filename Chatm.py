import requests
import time
print("Welcome to the Python Chat App!")
username = input("Enter your username: ")
SERVER_URL = "http://192.168.240.3:5000/chat"
def send_message():
	"""Send a message to the server"""
	msg = input("You: ")
	data = {"username": username, "message": msg}
	try:
		response = requests.post(SERVER_URL, json=data)
		print(f"[Data Link] Message sent ({response.status_code})")
	except:
		print("[Error] Could not reach server.")
def get_messages():
	"""Retrieve all messages from the server"""
	try:
		response = requests.get(SERVER_URL)
		messages = response.json()
		print("\n--- Chat Room ---")
		for m in messages:
			print(f"{m['username']}: {m['message']}")
		print("-----------------\n")
	except:
		print("[Error] Could not get messages from server")
while True:
	send_message()
	time.sleep(0.5)
	get_messages()
