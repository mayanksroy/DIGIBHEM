import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root=Tk()
root.title("Text To Speech App using Python")
root.geometry("900x450+280+200")
root.resizable(False,False)
root.config(bg="#999999")

image_icon = PhotoImage(file=r"TEXT_TO_SPEECH\icon.png")
root.iconphoto(False, image_icon)

Top_frame = Frame(root, bg="white", width=900, height=115)
Top_frame.place(x=0, y=0)

Logo=PhotoImage(file=r"TEXT_TO_SPEECH\icon1.png")
Label(Top_frame, image=Logo, bg="white").place(x=20, y=5)

Label(Top_frame, text="TEXT TO SPEECH", font="Ariel 20 bold italic", bg="white", fg="black").place(x=150, y=40)

text_area=Text(root, font="Robote 15", bg="white", fg="black", relief=GROOVE, wrap=WORD)
text_area.place(x=30, y=160, width=500, height=250)

gender_combobox=Combobox(root, values=["Male", "Female"], font="arial 14", state="r", width=10)
gender_combobox.place(x=550, y=200)
gender_combobox.set('Male')

speed_combobox=Combobox(root, values=["Fast", "Normal", "Slow"], font="arial 14", state="r", width=10)
speed_combobox.place(x=730, y=200)
speed_combobox.set('Normal')

root.mainloop()