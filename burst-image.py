import cv2
import os
import time
import threading
from tkinter import *
from PIL import Image, ImageTk

class BurstCameraApp:
    def __init__(self, root, save_dir="images/shocked", num_photos=5, delay=0.2):
        self.root = root
        self.root.title("📸 Burst Shot Camera")
        self.save_dir = save_dir
        self.num_photos = num_photos
        self.delay = delay
        self.cam = cv2.VideoCapture(0)
        self.is_capturing = False

        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)

        # --- GUI ELEMENTS ---
        self.preview_label = Label(root)
        self.preview_label.pack(padx=10, pady=10)

        self.button_frame = Frame(root)
        self.button_frame.pack()

        self.start_btn = Button(
            self.button_frame,
            text="Start Burst",
            command=self.start_burst,
            font=("Arial", 14),
            bg="#4CAF50",
            fg="white",
            padx=20,
            pady=5
        )
        self.start_btn.pack(side=LEFT, padx=10)

        self.counter_label = Label(
            self.button_frame,
            text="Photos: 0 / 0",
            font=("Arial", 12)
        )
        self.counter_label.pack(side=LEFT, padx=10)

        self.status_label = Label(root, text="", font=("Arial", 11), fg="gray")
        self.status_label.pack(pady=5)

        self.update_preview()

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    # --- Update camera feed preview ---
    def update_preview(self):
        ret, frame = self.cam.read()
        if ret:
            # Convert BGR → RGB for Pillow
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            self.preview_label.imgtk = imgtk
            self.preview_label.configure(image=imgtk)
        self.root.after(10, self.update_preview)

    # --- Burst capture in a separate thread ---
    def start_burst(self):
        if self.is_capturing:
            return
        self.is_capturing = True
        threading.Thread(target=self.capture_burst).start()

    def capture_burst(self):
        self.start_btn.config(state=DISABLED, bg="gray")
        self.status_label.config(text=f"📸 Taking {self.num_photos} photos...")
        timestamp = int(time.time())

        for i in range(self.num_photos):
            ret, frame = self.cam.read()
            if not ret:
                continue
            filename = os.path.join(self.save_dir, f"burst_{timestamp}_{i+1}.jpg")
            cv2.imwrite(filename, frame)
            self.counter_label.config(text=f"Photos: {i+1} / {self.num_photos}")
            time.sleep(self.delay)

        self.status_label.config(text="✅ Burst complete!")
        self.start_btn.config(state=NORMAL, bg="#4CAF50")
        self.is_capturing = False

    def on_close(self):
        self.cam.release()
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    app = BurstCameraApp(root, num_photos=300, delay=0.01)
    root.mainloop()
