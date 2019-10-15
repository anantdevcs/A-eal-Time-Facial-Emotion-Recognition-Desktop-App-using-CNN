from tkinter import *
from tkinter import font
import cv2
from PIL import Image, ImageTk

class WC:
    def __init__(self, master):
        self.master = master
        master.title("Smile!!")
        master.geometry("400x400")
        self.lmain = Label(master)
        self.lmain.grid()
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
        self.lmain.after(300, self.show_frame)




class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
        master.title('The game')
        master.geometry("400x400")
        helv36 = font.Font(family='Lucida Sans', size=36, weight='bold')
        self.label = Label(master, text="Welcome!",font=helv36,anchor="center")
        self.label.grid(row=1,column=2,columnspan=2)
        helv1 = font.Font(family='Lucida Sans', size=18, weight='bold')

        self.greet_button = Button(master, text="Start!", command=self.greet,font=helv1)
        self.greet_button.grid(row=3,column=4,columnspan=2)

        self.close_button = Button(master, text="Close", command=master.quit ,font=helv1)
        self.close_button.grid(row=4,column=4,columnspan=2)

    def greet(self):
        root = Tk()

        sec = WC(root)
        root.mainloop()
        print("Greetings!")
class Second:
    def __init__(self, master):
        self.master = master
        master.title("Hello World")

        self.label = Label(master, text="This is our 2nd GUI!")
        self.label.pack()

        


root = Tk()


my_gui = MyFirstGUI(root)

root.mainloop()

