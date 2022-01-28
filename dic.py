from PyDictionary import PyDictionary
import speech_rec as s
import text_to_speech as t
import threading
from tkinter import *

def main(word):
    dict = PyDictionary()
    
    meaning = dict.meaning(word)
    
    class App(threading.Thread):

        def __init__(self):
            threading.Thread.__init__(self)
            self.start()

        def callback(self):
            self.root.quit()

        def run(self):
            self.root = Tk()
            self.root.title('MEANING')
            
            l=Label(self.root,text=word+':'+str(meaning))
            l.pack()

            self.root.attributes('-topmost',True)
            self.root.after(7000, lambda: self.root.destroy())
            self.root.mainloop()
    App()
    t.speak(word)
    t.speak("is")
    t.speak(meaning)