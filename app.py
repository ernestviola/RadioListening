#!/usr/bin/env python2

# NOTE: this example requires PyAudio because it uses the Microphone class

import keyboard
import config as cfg
import sys
import time
import speech_recognition as sr
import threading
import send_sms
from twilio.rest import Client

def listen(r,m,audio):
    while listenTrue:
        sem.acquire()
        start_time = time.time()
        with m as source:
            audio = r.listen(source, phrase_time_limit = 7)
        sem.release()
        sem2.acquire()
        try:
            text = r.recognize_google(audio)
            print(text)
            f = open('output.txt','a+')
            f.write(' ' + text)
            f.close
        except sr.UnknownValueError:
            print("unable to recognize")
        sem2.release()

def analyzer():
    print("Starting analysis")
    while listenTrue:
        start_time = time.time()
        for _ in range(100): time.sleep(0.1)
        sem2.acquire()
        f = open("output.txt", "r+")
        text = f.read()
        f.seek(0)
        f.truncate()
        f.close()
        sem2.release()
        print("Analyzing...")
        print(text)
        text = text.lower()
        for word in stopWords:
            if word in text.lower():
                print("Keyword Found")
                for _ in range(240): time.sleep(0.1)
                sem2.acquire()
                f = open("output.txt", "r+")
                text += f.read()
                f.seek(0)
                f.truncate()
                f.close()
                sem2.release()
                send_sms.send(text)
                text = ""
                print("How long it took to form the message from hearing the keyword: ", time.time()-start_time)

def main():

    global f
    global listenTrue
    global sem
    global sem2
    global stopWords
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

    exit = raw_input("type \"exit\" to exit")

    if exit == "exit":
        listenTrue = False
        print("Waiting for threads to finish")
        for thread in threads:
            print("A thread finished")
            thread.join()
        print("We're done here")
        sys.exit()


if __name__ == '__main__':
   try:
      main()
   except KeyboardInterrupt:
      # do nothing here
      pass