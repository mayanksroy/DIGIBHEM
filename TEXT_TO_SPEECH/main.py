import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root=Tk()
root.title("Text To Speech App using Python")
root.geometry("900x450")
root.resizable(False,False)
root.config(bg="#999999")

image_icon = PhotoImage(file=r"TEXT_TO_SPEECH\icon.png")
root.iconphoto(False, image_icon)

Top_frame = Frame(root, bg="white", width=900, height=115)
Top_frame.place(x=0, y=0)

Logo=PhotoImage(file=r"TEXT_TO_SPEECH\icon1.png")
Label(Top_frame, image=Logo, bg="white").place(x=20, y=5)

root.mainloop()