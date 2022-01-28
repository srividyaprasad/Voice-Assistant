import pyjokes
import speech_recognition as s
import text_to_speech as t
def main():
    t.speak("Nerdy joke incoming")
    joke = pyjokes.get_joke(language="en", category="neutral")
    t.speak(joke)
    t.speak("Hope that made you laugh")