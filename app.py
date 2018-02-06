#!/usr/bin/env python2

# NOTE: this example requires PyAudio because it uses the Microphone class

import config as cfg
import datetime
import sys
import time
import speech_recognition as sr
import threading
import send_sms
from twilio.rest import Client
from collections import deque

def listen(r,m,audio):
    global numberTextToAnalyze
    while listenTrue:
        now = datetime.datetime.now()
        if now.minute <= 25:
            sem.acquire()
            with m as source:
                audio = r.listen(source, phrase_time_limit = 5)
            sem.release()
            sem2.acquire()
            try:
                text.append(r.recognize_google(audio))
                numberTextToAnalyze += 1
            except sr.UnknownValueError:
                pass
            sem2.release()

def analyzer():
    global numberTextToAnalyze
    print("Starting analysis")
    while listenTrue:
        now = datetime.datetime.now()
        if now.minute <= 30:
            if (numberTextToAnalyze == numberOfThreads):
                numberTextToAnalyze -=5
                print('\n',"Analyzing...", datetime.datetime.now(),'\n')
                for x in range(0,numberOfThreads):
                    phrase = text.popleft().lower()
                    print(phrase,end=" ")
                    for number in numbers:
                        for word in cfg.numbersKeywords[number]:
                            if word in phrase:
                                while True:
                                    if (numberTextToAnalyze == numberOfThreads):
                                        numberTextToAnalyze -=5
                                        for x in range(0,numberOfThreads):
                                            phrase += " " + text.popleft().lower()
                                        break
                                print('\n',phrase)
                                send_sms.send(phrase,number)

def main():

    global numbers
    global listenTrue
    global sem
    global sem2
    global threads
    global text
    global numberTextToAnalyze
    global numberOfThreads
    text = deque()
    numberTextToAnalyze = 0
    numberOfThreads = 5
    listenTrue = True
    sem = threading.Semaphore(value=1)
    sem2 = threading.Semaphore(value=1)
    numbers = list(cfg.numbersKeywords.keys()) #get all key values

    m = sr.Microphone()

    object1 = ''
    object2=''
    object3=''
    object4=''
    object5=''
    object6=''
    object7=''
    object8=''
    object9=''
    object10=''

    objects = [object1,object2,object3,object4,object5,object6,object7,object8,object9,object10]
    threads = []
    for i in range(numberOfThreads):
        print(i)
        thread = threading.Thread(target=listen,args=(sr.Recognizer(),m,objects[i]))
        threads.append(thread)
        thread.start()

    thread = threading.Thread(target=analyzer)
    threads.append(thread)
    thread.start()

    print("crtl + c to exit")

if __name__ == '__main__':
    main()