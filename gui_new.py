import tkinter as tk
from tkinter import scrolledtext
import cv2
import threading
import numpy as np
from PIL import Image, ImageTk

pi_ip = "192.168.240.123"
API = "http://192.168.240.123:5010"


class Quad:
    def __init__(self, root):
        self.root = root
        self.root.title("Quad GUI")
        self.root.geometry("1920x1080")

        # Layout frames
        self.top_left = tk.Frame(root, width=960, height=540, bg="black")
        self.top_left.grid(row=0, column=0, sticky="nsew")

        self.top_right = tk.Frame(root, width=960, height=540, bg="lightgray")
        self.top_right.grid(row=0, column=1, sticky="nsew")

        self.bottom_left = tk.Frame(root, width=960, height=540, bg="black")
        self.bottom_left.grid(row=1, column=0, sticky="nsew")

        self.bottom_right = tk.Frame(root, width=960, height=540, bg="white")
        self.bottom_right.grid(row=1, column=1, sticky="nsew")

        root.grid_rowconfigure(0, weight=1)
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)

        # Top left
    
        self.video1_label = tk.Label(self.top_left, bg="black")
        self.video1_label.pack(expand=True, fill=tk.BOTH)
        # Bottom left
        self.video2_label = tk.Label(self.bottom_left, bg="black")
        self.video2_label.pack(expand=True, fill=tk.BOTH)

        video_raw_url = f"{API}/video_raw"
        video_detect = f"{API}/video_processed"
        threading.Thread(target=self.update_video, args=(video_raw_url, self.video1_label), daemon=True).start()
        threading.Thread(target=self.update_video, args=(video_detect, self.video2_label), daemon=True).start()

        # Top right controls
        control_frame = tk.Frame(self.top_right, bg="lightgray")
        control_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Up button
        self.up_btn = tk.Button(
            control_frame,
            text="↑",
            font=("Arial", 20),
            width=5,
            height=2,
            command=lambda: self.button_click("goes forward")
        )
        self.up_btn.grid(row=0, column=2, pady=10)

        # Left button
        self.left_btn = tk.Button(
            control_frame,
            text="←",
            font=("Arial", 20),
            width=5,
            height=2,
            command=lambda: self.button_click("turns left")
        )
        self.left_btn.grid(row=1, column=0, padx=10)

        # Play button
        self.play_btn = tk.Button(
            control_frame,
            text="▶",
            font=("Arial", 20),
            width=5,
            height=2,
            fg="green",
            command=lambda: self.button_click("starts moving")
        )
        self.play_btn.grid(row=1, column=1, padx=10)

        # Stop button
        self.stop_btn = tk.Button(
            control_frame,
            text="■",
            font=("Arial", 20),
            width=5,
            height=2,
            fg="red",
            command=lambda: self.button_click("stops moving")
        )
        self.stop_btn.grid(row=1, column=3, padx=10)

        # Right button
        self.right_btn = tk.Button(
            control_frame,
            text="→",
            font=("Arial", 20),
            width=5,
            height=2,
            command=lambda: self.button_click("turns right")
        )
        self.right_btn.grid(row=1, column=4, padx=10)

        # Down button
        self.down_btn = tk.Button(
            control_frame,
            text="↓",
            font=("Arial", 20),
            width=5,
            height=2,
            command=lambda: self.button_click("goes backward")
        )
        self.down_btn.grid(row=2, column=2, pady=10)

        # Bottom right logs
        self.log_label = tk.Label(self.bottom_right, text="User Log", font=("Arial", 16))
        self.log_label.pack(pady=5)

        self.user_log = scrolledtext.ScrolledText(
            self.bottom_right, wrap=tk.WORD, width=100, height=25
        )
        self.user_log.pack(pady=10)

    def button_click(self, button_text):
        message = f"The robot {button_text}"
        self.add_log(message)

        try:
            with open("user_log.txt", "a") as log_file:
                log_file.write(message + "\n")
            print("write the user log successfully")
        except IOError as e:
            print(f"Error writing to file: {e}")

    def add_log(self, message):
        self.user_log.insert(tk.END, message + "\n")
        self.user_log.see(tk.END)
    def update_video(self, url, label):  
        cap = cv2.VideoCapture(url)
        while True:
            ret, frame = cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame)
                imgtk = ImageTk.PhotoImage(image=img)
    
                label.imgtk = imgtk
                label.config(image=imgtk)
            else:
                cap.release()
                cv2.waitKey(1000)
                cap = cv2.VideoCapture(url)

if __name__ == "__main__":
    root = tk.Tk()
    app = Quad(root)
    root.mainloop()
