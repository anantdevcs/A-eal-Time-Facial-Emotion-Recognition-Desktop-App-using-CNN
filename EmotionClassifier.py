# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 21:39:38 2019

@author: Anant Dev
"""

from Webcam import Webcam as WC
from tkinter import *
from tkinter import font
import cv2
from PIL import Image, ImageTk
#from tkinter.ttk import *


def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
class Welcome:
    def run_webam(self):
        top = Toplevel()
        Webcam = WC(top)
    def __init__(self, master):
        self.master = master
        master.title('Welcome')
        master.geometry("400x400")
        helv36 = font.Font(family='Lucida Sans', size=36, weight='bold')
        self.label = Label(master, text="Welcome!",font=helv36,anchor="center")
        self.label.config(anchor=CENTER)
        self.label.pack()
        helv1 = font.Font(family='Lucida Sans', size=18, weight='bold')
        self.greet_button = Button(master, text="Start!", command=self.run_webam,font=helv1)
        self.greet_button.config(anchor=CENTER)
        self.greet_button.pack()
        self.close_button = Button(master, text="Close", command=master.quit ,font=helv1)
        self.close_button.config(anchor=CENTER)
        self.close_button.pack()
        

#root = Tk()
## root.style = Style()
##('clam', 'alt', 'default', 'classic')
## root.style.theme_use("clam")
#center(root)
#this = Welcome(root)

#root.mainloop()
def run():
    root = Tk()
    center(root)
    Welcome_window = Welcome(root)
    root.mainloop()
    
run()




