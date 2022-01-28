from datetime import datetime
import text_to_speech as t

def main():
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    t.speak("The time is")
    t.speak(time)
    date, t1 = now.strftime("%d/%m/%Y, %H:%M:%S").split(',')
    t.speak("The date is")
    t.speak(date)