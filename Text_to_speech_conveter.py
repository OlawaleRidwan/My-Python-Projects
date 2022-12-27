import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox
import pyttsx3
import os



root = Tk()
root.title("TEXT TO SPEECH CONVERTER BY GROUP 18")
root.geometry("1000x580")
root.resizable(True,True) 
root.configure(bg = "#A020F0")


tts = pyttsx3.init()

def speaknow():
    text = text_box.get(1.0,END)
    gender = gender_box.get()
    speed = speed_box.get()
    voices = tts.getProperty('voices')
    def setvoice():
        if (gender=='Male'):
            tts.setProperty('voice',voices[0].id)
            tts.say(text)
            tts.runAndWait()
        else:
            tts.setProperty('voice',voices[1].id)
            tts.say(text)
            tts.runAndWait()
    if(text):
            if(speed=='Fast'):
                tts.setProperty('rate',250)
                setvoice()
            elif(speed == 'Medium'):
                tts.setProperty('rate',150)
                setvoice()
            else:
                tts.setProperty('rate',60)
                setvoice()

    

himark_logo = PhotoImage(file =r"C:\Users\HP\Desktop\hm.png")
Label(root, image = himark_logo, bg = "#F7AC40").place(x=1200,y=580)

logo_image =PhotoImage(file=r"C:\Users\HP\Desktop\speak.png")
root.iconphoto(False,logo_image)

upper_frame = Frame(root,bg = "#14A7DD",width = 1200, height = 130)
upper_frame.place(x=0,y=0)
picture =PhotoImage(file =r"C:\Users\HP\Desktop\hm.png")
Label(upper_frame, image = picture, bg = "#14A7DD").place(x = 150, y = 20)


Label(upper_frame, text = "Text to Speech Converter", font = "TimesNewroman 40 bold", bg ="#14A7DD", fg = 'white').place(x=300,y=35)

text_box = Text(root, font ="Calibti 20", bg = "white", relief =GROOVE,wrap = WORD,bd = 0 )
text_box.place(x=30, y= 150, width =940, height = 180)


gender_box = Combobox(root, values= ['Male', 'Female'], font ="Robote 12", state = 'r', width = 12)
gender_box.place(x = 340, y = 400)
gender_box.set('Male')


speed_box= Combobox(root, values = ['Fast', 'Medium', 'Slow'], font = "Robote 12", state = 'r', width = 12)
speed_box.place(x = 500, y = 400)
speed_box.set('Medium')


Label(root, text = "Select Voice", font = "TimesNewRoman 15 bold", bg = "#F7AC40", fg = "White").place(x = 340, y = 370)
Label(root, text = "Select Speed", font = 'TimesNewRoman 15 bold', bg = "#F7AC40", fg = "White").place( x =500, y = 370)



play_button = PhotoImage(file = r"C:\Users\HP\Desktop\imagen.png")
play_btn = Button(root, text="Play",compound =LEFT, image = play_button, bg = 'White', width = 130, font ="ariel 14 bold", borderwidth ='0.1c', command =speaknow)
play_btn.place(x=435, y = 450)
root.mainloop()
