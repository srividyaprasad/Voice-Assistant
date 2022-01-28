import speech_recognition as sr
r = sr.Recognizer()

def listen():
    while(1):	
        try:
            
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0)
                print('Listening...')
                audio = r.listen(source)
                print('Recognising...')
                MyText = r.recognize_google(audio)
                MyText = MyText.lower()

                print("User said: "+MyText)
                return MyText
                break      
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("Failed to recognise, please try again.")

       