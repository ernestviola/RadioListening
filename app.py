#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import time
import speech_recognition as sr
import threading

def listen(r,m,audio):
    while listenTrue:
        sem.acquire()
        start_time = time.time()
        with m as source:
            audio = r.listen(source, phrase_time_limit = 7)
        sem.release()
        sem2.acquire()
        try:
            f = open('output.txt','a+')
            f.write(' ' + r.recognize_google(audio))
            f.close
        except sr.UnknownValueError:
            pass
        sem2.release()

def analyzer():
    print("Starting analysis")
    while True:
        start_time = time.time()
        for _ in range(60): time.sleep(0.1)
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
                print("You found a vampire")
                for _ in range(240): time.sleep(0.1)
                sem2.acquire()
                f = open("output.txt", "r+")
                text += f.read()
                f.seek(0)
                f.truncate()
                f.close()
                sem2.release()
                print(text)
                text = ""
                print("How long it took to form the message from hearing the keyword: ", time.time()-start_time)

def main():

    global f
    global listenTrue
    global sem
    global sem2
    global stopWords
    stopWords = ["vampire","vampires"]
    listenTrue = True
    sem = threading.Semaphore(value=1)
    sem2 = threading.Semaphore(value=1)

    f = open('output.txt','w+')
    f.truncate()
    f.close()

    threads = []

    r = sr.Recognizer()
    output1 = ''
    r2 = sr.Recognizer()
    output2 = ''
    r3 = sr.Recognizer()
    output3 = ''
    r4 = sr.Recognizer()
    output4 = ''
    r5 = sr.Recognizer()
    output5 = ''
    r6 = sr.Recognizer()
    output6 = ''
    m = sr.Microphone()

    with m as source:
        r.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening

    t = threading.Thread(target=listen,args=(sr.Recognizer(),m,output1)).start()
    threads.append(t)
    t = threading.Thread(target=listen,args=(sr.Recognizer(),m,output2)).start()
    threads.append(t)
    t = threading.Thread(target=listen,args=(sr.Recognizer(),m,output3)).start()
    threads.append(t)
    t = threading.Thread(target=listen,args=(sr.Recognizer(),m,output4)).start()
    threads.append(t)
    t = threading.Thread(target=listen,args=(sr.Recognizer(),m,output5)).start()
    threads.append(t)
    t = threading.Thread(target=listen,args=(sr.Recognizer(),m,output6)).start()
    threads.append(t)

    t = threading.Thread(target=analyzer).start()

    if input() is "exit":
        listenTrue = False
        print("Waiting for the last listener")
        sys.exit()


if __name__ == '__main__':
   main()