#previous listener that uses pythons speech recognizer

import string
import threading
import speech_recognition as sr

from threading import Thread

# obtain audio
def voiceRecognition():
    while True:
        audioText = ''
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                audioText = r.recognize_google(audio)
                print(audioText)
            except sr.UnknownValueError:
                pass


if __name__ == '__main__':
    Thread(target = voiceRecognition).start()