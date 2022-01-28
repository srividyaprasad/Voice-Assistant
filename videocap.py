import cv2
import text_to_speech as t
def main():
    vid = cv2.VideoCapture(0)
    
    while(True):
        t.speak("Streaming video from webcam")
        ret, frame = vid.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    vid.release()
    cv2.destroyAllWindows()