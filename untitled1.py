# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 21:39:38 2019

@author: Dr. Mahendra Yadav
"""
from Webcam import Webcam as WC
from tkinter import *
from tkinter import font
import cv2
from PIL import Image, ImageTk

class Welcome:
    def run_webam(self):
            
            Webcam = WC(self.master)
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
        master.title('The game')
        master.geometry("400x400")
        helv36 = font.Font(family='Lucida Sans', size=36, weight='bold')
        self.label = Label(master, text="Welcome!",font=helv36,anchor="center")
        self.label.grid(row=1,column=2,columnspan=2)
        helv1 = font.Font(family='Lucida Sans', size=18, weight='bold')

        self.greet_button = Button(master, text="Start!", command=self.run_webam,font=helv1)
        self.greet_button.grid(row=3,column=4,columnspan=2)

        self.close_button = Button(master, text="Close", command=master.quit ,font=helv1)
        self.close_button.grid(row=4,column=4,columnspan=2)
        

root = Tk()
this = Welcome(root)

root.mainloop()




