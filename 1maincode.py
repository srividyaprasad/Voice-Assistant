import getweather, translation, dic, todolist, timedate, joke, calc, calcgui, grocerylist, alarm,  playmusic, takephoto, videocap, game, whatsappmsg
import speech_rec as s
import text_to_speech as t
import webbrowser, os
from tkinter import *
import threading

t.speak("Hello, I'm Jarvis, your personal voice assistant. What is your name?")
name=s.listen()
t.speak("Is this your first time using me?")
ans=s.listen()
if "yes" in ans:
    t.speak("Nice to meet you!")
    t.speak(name)
    t.speak("I can help you with a bunch of things. Here's how you can ask")
    t.speak("Jarvis, play a song. Jarvis, take a picture. Jarvis, update my to do list. Jarvis, set an alarm. ")
    #Jarvis, tell me what the weather is like. Jarvis, translate something. Jarvis, search computer on youtube. Jarvis, whats the time and date. Jarvis, locate bangalore. Jarvis, open ms word. Jarvis, search food on google. Jarvis, calculate something for me. Jarvis, update my grocery list. Jarvis, stream live video from webcam.")
    
else:
    t.speak("Welcome back, old friend")
t.speak("Go ahead")
t.speak(name)

while True:
    response=s.listen().lower()
    resplist=response.split()
    if "jarvis" in resplist:

        if "weather" in resplist: #tell me the weather in city country
            city=resplist[resplist.index('weather')+2]
            country=resplist[resplist.index('weather')+3]
            getweather.main(city, country)

        elif "translate" in resplist: #translate word to language
            word=resplist[resplist.index('translate')+1]
            lang=resplist[resplist.index('translate')+3]
            translation.main(word, lang)

        elif "meaning" in resplist: #meaning of word
            word=resplist[resplist.index('meaning')+2]
            dic.main(word)

        elif "do" in resplist: #add task to my to do list
            task=''
            if 'add' in resplist:
                x='add'
                item=response[5, response.index('to')+1]
            if 'remove' in resplist:
                x='remove'
                item=response[7, response.index('from')+1]
            if 'read' in resplist:
                x='read'
                task=''
            todolist.main(x, task)

        elif "grocery" in resplist: #add item to my grocery list
            item=''
            if 'add' in resplist:
                x='add'
                item=response[5, response.index('to')+1]
            if 'remove' in resplist:
                x='remove'
                item=response[7, response.index('from')+1]
            if 'read' in resplist:
                x='read'
                item=''
            grocerylist.main(x, item)

        elif "time" in resplist or "date" in resplist: #jarvis whats the time 
            timedate.main()

        elif "joke" in resplist or "laugh" in resplist: #jarvis make me laugh
            joke.main()
        
        elif "calculate" in resplist: #jarvis i want you to calculate something
            calc.main()

        elif "calculator" in resplist: #jarvis open calculator
            calcgui.main()
        
        elif "alarm" in resplist: #jarvis i want to set an alarm
            alarm.main()
        
        elif "song" in resplist or "music" in resplist: #play sweetener from my music #play sweetener song
            song=resplist[resplist.index('play')+1]
            playmusic.main(song)
            
        elif "picture" in resplist or "photo" in resplist: #jarvis take a picture
            takephoto.main() 
        
        elif "video" in resplist: 
            videocap.main()
                
        elif "bye" in resplist or "stop" in resplist: #jarvis stop
            t.speak("Goodbye")
            t.speak(name)
            break

        elif "game" in resplist: #jarvis i want to play a game with you
            game.main()

        elif "whatsapp" in resplist or "message" in resplist: #jarvis send whatsapp message hello
            if 'message' in resplist:
                msg=resplist[resplist.index('message')+1]
            else:
                msg='Hello!'
            whatsappmsg.main(msg)

        elif "locate" in resplist: #locate delhi on map
            location = resplist[resplist.index('locate')+1]
            webbrowser.open("https://www.google.com/maps/place/"+location)

        elif "search" in resplist:
            if "youtube" in resplist: 
                query = location = resplist[resplist.index('youtube')-2]
                t.speak("Searching")
                t.speak(query)
                t.speak("on youtube")
                url = "https://www.youtube.com/results?search_query="+query
                webbrowser.open(url)

            elif 'wikipedia' in resplist:

                query = location = resplist[resplist.index('wikipedia')-2]
                t.speak("Searching")
                t.speak(query)
                t.speak("on wikipedia")
                url= "https://en.wikipedia.org/wiki/"+query
                webbrowser.open(url)

            elif 'google' in resplist:

                query = location = resplist[resplist.index('google')-2]
                t.speak("Searching")
                t.speak(query)
                t.speak("on google")
                url = "https://www.google.com.tr/search?q="+query
                webbrowser.open(url)
            
        elif "open" in resplist:

            if "word" in resplist:
                t.speak("Opening Microsoft Word")
                os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE")


            elif "excel" in resplist:
                t.speak("Opening Microsoft Excel")
                os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE")

            elif "powerpoint" in resplist:
                t.speak("Opening Microsoft Powerpoint")
                os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE")

        else:
                t.speak("I dont understand, shall I search this on the web?")
                ans = s.listen()
                if 'yes' in ans:
                    response.replace("jarvis ","")
                    webbrowser.open("https://www.google.com/"+response)

                else:
                    t.speak("Okay")