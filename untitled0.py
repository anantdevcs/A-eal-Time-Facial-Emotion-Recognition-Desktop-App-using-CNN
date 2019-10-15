from tkinter import *
import cv2
from PIL import Image, ImageTk

class Webcam:
    def __init__(self, master):
        self.master = master
        master.title("Smile!!")
        master.geometry("800x600")
        self.lmain = Label(master)
        self.lmain.grid(row=2,column=2)
        width, height = 800, 600
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.show_frame()

    def show_frame(self):
        _, frame = self.cap.read()
        frame = cv2.flip(frame, 1)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        self.lmain.imgtk = imgtk
        self.lmain.configure(image=imgtk)
        self.lmain.after(200, self.show_frame)

root = Tk()
i=Webcam(root)
root.mainloop()
