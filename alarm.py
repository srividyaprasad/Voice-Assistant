# Importing required libraries
from datetime import datetime   #To set date and time
from playsound import playsound     #To play sound
import speech_rec as s
import text_to_speech as t
from tkinter import *
from tkinter import messagebox
import threading
root=Tk()
name_var=StringVar()

def main():

    def validate_time(alarm_time):
        if len(alarm_time) != 8:
            return "Invalid time format! Please try again..."
        else:
            if int(alarm_time[0:2]) > 12 or int(alarm_time[3:5]) > 59:
                return "Invalid time format! Please try again..."
            else:
                return "ok"

    while True:
        t.speak("Sure, enter the time to set alarm")
        def submit():
            root.after(1000,lambda:root.destroy())
            return name_var.get()
        name_label = Label(root, text = 'Enter time in HH:MM AM/PM format: ')
        name_entry = Entry(root, textvariable = name_var)
        sub_btn=Button(root,text = 'Submit',command=submit)

        name_label.grid(row=0,column=0)
        name_entry.grid(row=0,column=1)
        sub_btn.grid(row=0,column=2)

        root.mainloop()
        alarm_time = submit()
        validate = validate_time(alarm_time.lower())
        if validate != "ok":
            t.speak(validate)
        else:
            t.speak("Alarm set for")
            t.speak(alarm_time)
            break

    alarm_hour = alarm_time[0:2]
    alarm_min = alarm_time[3:5]
    alarm_period = alarm_time[6:].upper()

    while True:
        now = datetime.now()

        current_hour = now.strftime("%I")
        current_min = now.strftime("%M")
        current_period = now.strftime("%p")

        if alarm_period == current_period:
            if alarm_hour == current_hour:
                if alarm_min == current_min:
                        t.speak("Wake Up!")
                        playsound(r'C:\Users\srivi\OneDrive\Desktop\miniproject/alarmsound.wav')
                        window=Tk()
                        window.eval('tk::PlaceWindow %s centre' % window.winfo_toplevel())
                        window.withdraw()
                        messagebox.showinfo('This Is Your Alarm', 'Its Time To Get Up')

                        window.quit()
                        break