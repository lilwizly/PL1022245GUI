import tkinter as tk
from tkinter import scrolledtext
class Quad:
  def __init__(self, root):
    self.root = root
    self.root.title("Quad GUI")
    self.root.geometry("1920x1080")
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
#Top left
    self.video1_label = tk.Label(self.top_left, text="Video Stream 1", fg="white", bg="black",
font=("Arial", 24))
    self.video1_label.place(relx=0.5, rely=0.5, anchor="center")
#Buttom left
    self.video2_label = tk.Label(self.bottom_left, text="Video Stream 2", fg="white", bg="black",
font=("Arial", 24))
    self.video2_label.place(relx=0.5, rely=0.5, anchor="center")
#Top right
    control_frame = tk.Frame(self.top_right, bg="lightgray")
    control_frame.place(relx=0.5, rely=0.5, anchor="center")
#UpButton
    self.up_btn = tk.Button(control_frame, text="↑", font=("Arial", 20), width=5, height=2)
    self.up_btn.grid(row=0, column=2, pady=10)
#LeftButton
    self.left_btn = tk.Button(control_frame, text="←", font=("Arial", 20), width=5, height=2)
    self.left_btn.grid(row=1, column=0, padx=10)
#PlayButton
    self.play_btn = tk.Button(control_frame, text="▶", font=("Arial", 20), width=5, height=2,
fg="green")
    self.play_btn.grid(row=1, column=1, padx=10)
#StopButton
    self.stop_btn = tk.Button(control_frame, text="■", font=("Arial", 20), width=5, height=2,
fg="red")
    self.stop_btn.grid(row=1, column=3, padx=10)
#RightButton
    self.right_btn = tk.Button(control_frame, text="→", font=("Arial", 20), width=5, height=2)
    self.right_btn.grid(row=1, column=4, padx=10)
#DownButton
    self.down_btn = tk.Button(control_frame, text="↓", font=("Arial", 20), width=5, height=2)
    self.down_btn.grid(row=2, column=2, pady=10)
#Bottom right
    self.log_label = tk.Label(self.bottom_right, text="User Log", font=("Arial", 16))
    self.log_label.pack(pady=5)
    self.user_log = scrolledtext.ScrolledText(self.bottom_right, wrap=tk.WORD, width=100,
height=25)
    self.user_log.pack(pady=10)
    self.add_log("log123")
  def add_log(self, message):
    self.user_log.insert(tk.END, message + "\n")
    self.user_log.see(tk.END)
if __name__ == "__main__":
  root = tk.Tk()
  app = Quad(root)
  root.mainloop()
