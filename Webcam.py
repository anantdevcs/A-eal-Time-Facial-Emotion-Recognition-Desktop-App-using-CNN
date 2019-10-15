from tkinter import *
import cv2
from PIL import Image, ImageTk

class Webcam:
    def __init__(self, master):
        self.master = master
        master.title("Smile!!")
        master.geometry("800x600")
        self.lmain = Label(master)
        self.lmain.config(anchor=CENTER)
        self.lmain.pack()
        self.setup()
    def setup(self):
        width, height = 800, 600
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.read_faces()

    def read_faces(self):
        _, frame = self.cap.read()
        frame = cv2.flip(frame, 1)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        self.lmain.imgtk = imgtk
        self.lmain.configure(image=imgtk)
        self.lmain.after(200, self.read_faces)
        
    def detect_faces(self , img):
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
        for (x,y,w,h) in faces: 
            # To draw a rectangle in a face  
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)  
            roi_gray = gray[y:y+h, x:x+w] 
            roi_color = img[y:y+h, x:x+w] 

        
        
        
   
             
             
             

#root = Tk()
#i=Webcam(root)
#root.mainloop()
