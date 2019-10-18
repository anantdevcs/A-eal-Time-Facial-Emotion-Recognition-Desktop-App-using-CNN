# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 21:39:38 2019
@author: Anant Dev
"""

from Webcam import Webcam as WC
from tkinter import *
from tkinter import font
import cv2
import tkinter
from PIL import Image, ImageTk


class Welcome:
    def run_webam(self):
        top = Toplevel()
        Webcam = WC(top)
    def __init__(self, master):
        self.master = master
        master.title('Face Emotion App')
        master.geometry("400x400")
        image=Image.open('FacePic.png')
        image = image.resize((250, 250), Image.ANTIALIAS) ## The (250, 250) is (height, width)
        self.bgimg = ImageTk.PhotoImage(image)
        self.panel = Label(master, image = self.bgimg)
        self.panel.pack(side = "bottom")
        helv36 = font.Font(family='Lucida Sans', size=36, weight='bold')
        self.label = Label(master, text="Welcome!",font=helv36,anchor="center")
        self.label.config(anchor=CENTER)
        self.label.pack()
        helv1 = font.Font(family='Lucida Sans', size=18, weight='bold')
        self.greet_button = Button(master, text="Start!", command=self.run_webam,font=helv1)
        self.greet_button.config(anchor=CENTER)
        self.greet_button.pack(side="top")
        self.close_button = Button(master, text="Close", command=master.quit ,font=helv1)
        self.close_button.config(anchor=CENTER)
        self.close_button.pack(side="bottom")
     
#Helper Functon for center aligning main window   
def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def run():
    root = Tk()
    center(root)
    root.resizable(False, False)
    Wel = Welcome(root)

    root.mainloop()
    
run()