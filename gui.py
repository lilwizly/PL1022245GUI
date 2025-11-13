import tkinter as tk
from tkinter import scrolledtext
import requests
import cv2
from PIL import Image, ImageTk

API_URL = "http://127.0.0.1:5000"

class Quad:
    def __init__(self, root):
        self.root = root
        self.root.title("Robot Controller GUI")
        self.root.geometry("1280x720")

        # Quadrants
        self.top_left = tk.Frame(root, width=640, height=360, bg="black")
        self.top_left.grid(row=0, column=0, sticky="nsew")

        self.top_right = tk.Frame(root, width=640, height=360, bg="lightgray")
        self.top_right.grid(row=0, column=1, sticky="nsew")

        self.bottom_left = tk.Frame(root, width=640, height=360, bg="black")
        self.bottom_left.grid(row=1, column=0, sticky="nsew")

        self.bottom_right = tk.Frame(root, width=640, height=360, bg="white")
        self.bottom_right.grid(row=1, column=1, sticky="nsew")

        root.grid_rowconfigure(0, weight=1)
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)

        # VIDEO STREAMS
        self.cap = cv2.VideoCapture(0)

        # create 2 video labels
        self.video1_label = tk.Label(self.top_left)
        self.video1_label.pack(fill="both", expand=True)

        self.video2_label = tk.Label(self.bottom_right)
        self.video2_label.pack(fill="both", expand=True)

        #CONTROL PANEL (top-right quadrant)
        control_frame = tk.Frame(self.top_right, bg="lightgray")
        control_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.up_btn = tk.Button(control_frame, text="↑", font=("Arial", 20), width=5, height=2, command=self.forward)
        self.up_btn.grid(row=0, column=2, pady=10)

        self.left_btn = tk.Button(control_frame, text="←", font=("Arial", 20), width=5, height=2, command=self.left)
        self.left_btn.grid(row=1, column=0, padx=10)

        self.play_btn = tk.Button(control_frame, text="▶", font=("Arial", 20), width=5, height=2, fg="green", command=self.start)
        self.play_btn.grid(row=1, column=1, padx=10)

        self.stop_btn = tk.Button(control_frame, text="■", font=("Arial", 20), width=5, height=2, fg="red", command=self.stop)
        self.stop_btn.grid(row=1, column=3, padx=10)

        self.right_btn = tk.Button(control_frame, text="→", font=("Arial", 20), width=5, height=2, command=self.right)
        self.right_btn.grid(row=1, column=4, padx=10)

        self.down_btn = tk.Button(control_frame, text="↓", font=("Arial", 20), width=5, height=2, command=self.backward)
        self.down_btn.grid(row=2, column=2, pady=10)

        # USER LOG (bottom-left quadrant)
        self.log_label = tk.Label(self.bottom_left, text="User Log", font=("Arial", 16), bg="black", fg="white")
        self.log_label.pack(pady=5)

        self.user_log = scrolledtext.ScrolledText(self.bottom_left, wrap=tk.WORD, width=60, height=15)
        self.user_log.pack(pady=10)

        self.add_log("System Ready.")

        # Start video update loop
        self.update_videos()

    #VIDEO UPDATE
    def update_videos(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)

            self.video1_label.imgtk = imgtk
            self.video1_label.config(image=imgtk)

            self.video2_label.imgtk = imgtk
            self.video2_label.config(image=imgtk)
        #raload after 30 seconds
        self.root.after(30, self.update_videos)

    # --- API FUNCTIONS ---
    def send_command(self, endpoint):
        try:
            res = requests.get(f"{API_URL}/{endpoint}")
            if res.status_code == 200:
                data = res.json()
                self.add_log(f"{data['comment']}")
            else:
                self.add_log(f"Error {res.status_code}: {res.text}")
        except Exception as e:
            self.add_log(f"API Error: {e}")

    def add_log(self, message):
        self.user_log.insert(tk.END, message + "\n")
        self.user_log.see(tk.END)

    def forward(self): self.send_command("forward")
    def backward(self): self.send_command("backward")
    def left(self): self.send_command("left")
    def right(self): self.send_command("right")
    def stop(self): self.send_command("stop")
    def start(self): self.send_command("start")

    def __del__(self):
        if self.cap.isOpened():
            self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = tk.Tk()
    app = Quad(root)
    root.mainloop()

