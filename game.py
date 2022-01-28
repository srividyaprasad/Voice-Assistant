import random
import speech_rec as s
import text_to_speech as t
def main():
    n = random.randint(1, 100)
    t.speak("Guess a number between 1 and 100")
    while 1:
        guess = int(s.listen())
        if guess < n:
            t.speak("Too low")
        elif guess > n:
            t.speak("Too high")
        else:
            t.speak("That's right!")
            break