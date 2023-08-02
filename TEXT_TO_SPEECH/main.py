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

engine = pyttsx3.init()

def speaknow():
    text=text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')
    
    def setvoice():
        if(gender == 'Male'):
            engine.setProperty('voice', voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            engine.say(text)
            engine.runAndWait()
    if(text):
        if(speed == 'Fast'):
            engine.setProperty('rate',250)
            setvoice()
        elif(speed == 'Normal'):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()
              
def download():
    text=text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')
    
    def setvoice():
        if(gender == 'Male'):
            engine.setProperty('voice', voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, 'audio_to_text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, 'audio_to_text.mp3')
            engine.runAndWait()
    if(text):
        if(speed == 'Fast'):
            engine.setProperty('rate',250)
            setvoice()
        elif(speed == 'Normal'):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()

image_icon = PhotoImage(file=r"TEXT_TO_SPEECH\icon.png")
root.iconphoto(False, image_icon)

Top_frame = Frame(root, bg="white", width=900, height=115)
Top_frame.place(x=0, y=0)

Logo=PhotoImage(file=r"TEXT_TO_SPEECH\icon1.png")
Label(Top_frame, image=Logo, bg="white").place(x=10, y=5)

Logo2=PhotoImage(file=r"TEXT_TO_SPEECH\icon1.png")
Label(Top_frame, image=Logo, bg="white").place(x=780, y=5)

Label(Top_frame, text="TEXT TO SPEECH APPLICATION", font="Comic-Sans-MS 25 bold", bg="white", fg="black").place(x=180, y=35)

text_area=Text(root, font="Robote 15", bg="white", fg="black", relief=GROOVE, wrap=WORD)
text_area.place(x=30, y=160, width=500, height=250)

Label(root, text="VOICE", font="ariel 15 bold", bg="#999999", fg="white").place(x=580, y=170)
Label(root, text="SPEED", font="ariel 15 bold", bg="#999999", fg="white").place(x=760, y=170)

gender_combobox=Combobox(root, values=["Male", "Female"], font="arial 14", state="r", width=10)
gender_combobox.place(x=550, y=200)
gender_combobox.set('Male')

speed_combobox=Combobox(root, values=["Fast", "Normal", "Slow"], font="arial 14", state="r", width=10)
speed_combobox.place(x=730, y=200)
speed_combobox.set('Normal')

imageicon=PhotoImage(file=r"TEXT_TO_SPEECH\speaking.png")
btn=Button(root, compound=LEFT, image=imageicon, font="arial 14 bold", command=speaknow)
btn.place(x=580, y=280)
Label(root, text="SPEAK", font="ariel 15 bold", bg="#999999", fg="white").place(x=572, y=335)

imageicon2=PhotoImage(file=r"TEXT_TO_SPEECH\download.png")
btn=Button(root, compound=LEFT, image=imageicon2, font="arial 14 bold", command=download)
btn.place(x=760, y=280)
Label(root, text="SAVE", font="ariel 15 bold", bg="#999999", fg="white").place(x=758, y=335)

root.mainloop()