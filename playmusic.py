from pygame import mixer

import text_to_speech as t
from tkinter import *
import pygame


def main(song):
    root = Tk()
    root.title('MUSIC PLAYER')
    
    t.speak("Playing "+song+" from the folder My Music")
    while True:
        mixer.init()
        songpath=r'C:\Users\srivi\OneDrive\Desktop\miniproject\My Music\\'
        songpath+=song
        songpath+=".ogg"
        mixer.music.load(songpath)


        def play():
            pygame.mixer.music.load(songpath)
            pygame.mixer.music.play()

        global paused
        paused = False
        def pause(is_paused):
            global paused
            paused = is_paused

            if paused:
                pygame.mixer.music.unpause()
                paused = False
            else:
                pygame.mixer.music.pause()
                paused = True

        def stop():
            pygame.mixer.music.stop()

        a = PhotoImage(file=r'C:\Users\srivi\OneDrive\Desktop\miniproject\play.gif')
        b = PhotoImage(file=r'C:\Users\srivi\OneDrive\Desktop\miniproject\pause.gif')
        c = PhotoImage(file=r'C:\Users\srivi\OneDrive\Desktop\miniproject\stop.gif')

        Control_Frame = Frame(root, padx=10, pady=10, highlightbackground="black", highlightthickness=3)
        Control_Frame.pack(padx=20, pady=20)

        play_button = Button(Control_Frame, image=a, borderwidth=0, command=play)
        pause_button = Button(Control_Frame, image=b, borderwidth=0, command=lambda: pause(paused))
        stop_button = Button(Control_Frame, image=c, borderwidth=0, command=stop)

        play_button.grid(row=0, column=0, padx=5)
        pause_button.grid(row=0, column=1, padx=5)
        stop_button.grid(row=0, column=2, padx=5)

        root.mainloop()