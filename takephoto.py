import cv2
import os
import speech_recognition as s
import text_to_speech as t
def main():
    path, dirs, files = next(os.walk(r"C:\Users\srivi\OneDrive\Desktop\miniproject\My Gallery"))
    n = len(files)
    t.speak("Taking picture in 3... 2.... 1")
    hi = cv2.VideoCapture(0)
    a, b = hi.read()
    b = cv2.flip(b,1)
    cv2.imshow("Hello", b)
    path=r"C:\Users\srivi\OneDrive\Desktop\miniproject\My Gallery\pic"+str(n+1)+".jpg"
    cv2.imwrite(path,b)
    t.speak("Picture saved to folder My Gallery")