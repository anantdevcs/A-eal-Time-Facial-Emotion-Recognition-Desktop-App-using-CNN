from tkinter import *
import cv2
from PIL import Image, ImageTk
import tensorflow as tf
import numpy as np
from tkinter import font
from tkinter import messagebox

class Webcam:
    def __init__(self, master):
        self.master = master
        self.ans = Label(master)
        self.ans.pack()
        self.final = Label(master)
        self.final.pack(side="bottom")
        self.helv36 = font.Font(family='Lucida Sans', size= 11, weight='bold')
        master.title("Smile!!")
        master.geometry("800x600")
        self.labels=['Angry','Disgust','Fear','Happy','Sad','Surprise','Neutral']
        self.lmain = Label(master )
        self.lmain.config(anchor=CENTER )
        self.lmain.pack()
        self.load_model()
        self.setup()
    def detect_faces(self , img):
    	#Returns an image with rectangle drawn around it AND a list of cropped faces
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
        face_list=[]
        for (x,y,w,h) in faces: 
            # To draw a rectangle in a face  
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
            face_list.append(img[y:y+h, x:x+w])        
        
        return img,face_list
    
        
    def setup(self):
    	#Setup the Webcam
        width, height = 800, 600
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.read_faces()

    def read_faces(self):
        _, frame = self.cap.read()
        frame = cv2.flip(frame, 1)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        cv2image , face_list=self.detect_faces(cv2image)
        self.evaluate_expression(face_list)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        self.lmain.imgtk = imgtk
        self.lmain.configure(image=imgtk)
        #200 = 200ms 
        #This means frames change after every 200ms or 0.2s
        self.lmain.after(200, self.read_faces)
        
    def load_model(self):
    	try:
    		self.model = tf.keras.models.load_model('model_v6_23.hdf5')
    	except Exception as e:
    		messagebox.showerror("Error", "The specified h5 model not found") 

        
        
    def evaluate_expression(self,face_list):
    	#The current version of the code only Evaluates Facial Expression
    	#recognition on one face at a time
    	#Nevertheless face_list is passed as a list of cropped faces
        for face in face_list:
            gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            resized = cv2.resize(gray, (48,48), interpolation = cv2.INTER_AREA)
            resized=resized.reshape(1,48,48,1)
            resized=resized/255.00 #Necessary Preprocessing!
            prediction = self.model.predict(resized) #This is the predictions vector
            emotion_now = (self.labels[np.argmax(prediction)])
            self.master.title("You Look "+ str(emotion_now))
            self.final.config(text=str(emotion_now) , fg="red",font = self.helv36)
            stmt="" # The string to be displayed on a label
            for i in range(7):
                stmt = stmt + str(self.labels[i]) + "  " + str(int(prediction[0,i]*100.00)) + "\n"
            self.ans.config(text=stmt ,  font = self.helv36)
                