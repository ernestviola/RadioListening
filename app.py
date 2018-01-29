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

def listen(r,m,audio):
    while listenTrue:
        sem.acquire()
        with m as source:
            audio = r.listen(source, phrase_time_limit = 7)
        sem.release()
        sem2.acquire()
        try:
            text = r.recognize_google(audio)
            f = open('output.txt','a+')
            f.write(' ' + text)
            f.close
        except sr.UnknownValueError:
            pass
        sem2.release()

def analyzer():
    print("Starting analysis")
    while listenTrue:
        start_time = time.time()
        time.sleep(7.0) #sleep for at least 10 seconds between each analysis
        sem2.acquire()
        f = open("output.txt", "r+")
        text = f.read()
        f.seek(0)
        f.truncate()
        f.close()
        sem2.release()
        print("Analyzing...", datetime.datetime.now(),'\n',text)
        text = text.lower()
        for word in stopWords:
            if word in text.lower():
                print("Keyword Found")
                time.sleep(25.0)
                sem2.acquire()
                f = open("output.txt", "r+")
                text += f.read()
                f.seek(0)
                f.truncate()
                f.close()
                sem2.release()
                send_sms.send(text) #Sends recorded message to list of numbers
                text = ""
                print("How long it took to form the message from hearing the keyword: ", time.time()-start_time)

def main():

    global f
    global listenTrue
    global sem
    global sem2
    global stopWords
    global threads
    numberOfThreads = 10
    stopWords = cfg.configuration['keywords']
    listenTrue = True
    sem = threading.Semaphore(value=1)
    sem2 = threading.Semaphore(value=1)

    m = sr.Microphone()

    f = open('output.txt','w+')
    f.truncate()
    f.close()
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