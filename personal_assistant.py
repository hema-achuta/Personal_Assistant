"""import speech_recognition as sr

r = sr.Recognizer()
m = sr.Microphone()

try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        print("Say something!")
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)

            # we need some special handling here to correctly print unicode characters to standard output
            if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                print(u"You said {}".format(value).encode("utf-8"))
            else:  # this version of Python uses unicode for strings (Python 3+)
                print("You said {}".format(value))
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass"""
import datetime
import os
import pprint
import time
import json
import requests
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import smtplib
import pyautogui
import webbrowser
import pyjokes
import wolframalpha
import urllib.request
import win32com.client as wincl
import cv2
import pygame
import pygame.camera
import subprocess


from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup



r = sr.Recognizer()
m = sr.Microphone()
e = pyttsx3.init()
rate = e.getProperty('rate')
e.setProperty('rate', rate + 10)
#v = e.getProperty('voices')
#e.setProperty('voice',v[1].id)
hour = int(datetime.datetime.now().hour)
if hour>=0 and hour<12:
    e.say('Good morning')
elif hour>=12 and hour<18:
    e.say("good afternoon")
else:
    e.say("Good evening")
e.say('hiii iam krish')

e.runAndWait()


def talk(text):
    e.say(text)
    e.runAndWait()


def take():
    try:
        with m as source:
            print('listening')
            voice = r.listen(source)
            comm = r.recognize_google(voice)
            comm = comm.lower()
            print(comm)
            talk(comm)
    except:
        pass
    return comm


def cc(question):

       # question = input('Question: ')
    app_id = '7W3TA9-2YTVLJL865'
    client = wolframalpha.Client(app_id)
    res = client.query(question)
    answer = next(res.results).text
    print(answer)
    talk(answer)


def NewsFromBBC():
    # BBC news api
    # following query parameters are used
    # source, sortBy and apiKey
    query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "4dbc17e007ab436fb66416009dfb59a8"
    }
    main_url = " https://newsapi.org/v1/articles"

    # fetching data in json format
    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()

    # getting all articles in a string article
    article = open_bbc_page["articles"]

    # empty list which will
    # contain all trending news
    results = []

    for ar in article:
        results.append(ar["title"])

    for i in range(len(results)):
        # printing all trending news
        print(i + 1, results[i])

    # to read the news out loud for us
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.Spvoice")
    speak.Speak(results)





def run_kris():
    comm = take()
    print(comm)
    if 'play' in comm:

        song = comm.replace('play','')
        talk('playing'+song)
        print('playing')
        print(song)
        pywhatkit.playonyt(song)
    elif 'time' in comm:
        ti = datetime.datetime.now().strftime('%H:%M %p')
        print(ti)
        talk('current time is'+ti)
    elif 'who is ' in comm:
        per = comm.replace('who is','')
        info = wikipedia.summary(per,5)
        print(info)
        talk(info)
    elif 'send  whatsapp message' in comm:
        talk('please enter reciever phonenumber')
        g = input("enter phonenumber along with countrycode")
        talk("Enter the time at which you want to send the message")
        k = input("enter time")
        talk("Enter the message u want to send")
        message = input()
        pywhatkit.sendwhatmsg(g,k,20,38)

    elif 'open google' in comm:
        talk('opening google')
        url = "https://www.geeksforgeeks.org"
        webbrowser.open(url)
    elif 'open linkedin' in comm:
        talk('opening linkedin')
        url = "https://in.linkedin.com/nhome/"
        webbrowser.open(url)
    elif 'open github' in comm:
        talk('opening github')
        url = "https://github.com/"
        webbrowser.open(url)
    elif 'tell a joke' in comm:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif 'going on' in comm or 'news' in comm or 'headlines' in comm:
        NewsFromBBC()
    elif 'capture' in comm:
        pygame.camera.init()
        camlist = pygame.camera.list_cameras()
        if camlist:
            cam = pygame.camera.Camera(camlist[0], (640, 480))
            cam.start()
            image = cam.get_image()
            pygame.image.save(image, "hema.jpg")
        else:
            print("No camera on current device")


    elif 'calculate' in comm or 'what is' in comm or 'temperature'   in comm:
        a = str(comm)
        a = a.replace("krish","")
        a = a.replace("krrish", "")
        a = a.replace("calculate","")
        a = a.replace("multiply","*")
        a = a.replace("divided by","/")
        a = a.replace("add","+")
        a = a.replace("substract","-")
        a = a.replace("into","*")
        a = a.replace("plus","+")
        a = a.replace("minus","-")
        cc(str(a))

    elif "log of" in comm or "sign out" in comm:
        talk("Ok , your pc will log off in 10 sec make sure you exit from all applications")
        subprocess.call(["shutdown", "/l"])
        time.sleep(3)



    else:
        talk("please try saying it again")


run_kris()






