from translate import Translator
import speech_rec as s
import text_to_speech as t
from tkinter import *
import threading

def main(word, lang):
    
    
    translator= Translator(lang)
    translation = translator.translate(word)
    
    class App(threading.Thread):

        def __init__(self):
            threading.Thread.__init__(self)
            self.start()

        def callback(self):
            self.root.quit()

        def run(self):
            self.root = Tk()
            self.root.title('TRANSLATION')
            
            l=Label(self.root,text=word+' in '+lang+':'+translation)
            l.pack()

            self.root.attributes('-topmost',True)
            self.root.after(7000, lambda: self.root.destroy())
            self.root.mainloop()
    App()
    t.speak(word)
    t.speak('in')
    t.speak(lang)
    t.speak('is')
    t.speak(translation)