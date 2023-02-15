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
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import smtplib
import webbrowser


r = sr.Recognizer()
m = sr.Microphone()
e = pyttsx3.init()
#v = e.getProperty('voices')
#e.setProperty('voice',v[1].id)
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
    elif 'send message' in comm:
        talk('please enter reciever phonenumber')
        g = input("enter phonenumber along with countrycode")
        talk("Enter the time at which you want to send the message")
        k = input("enter time")
        talk("Enter the message u want to send")
        message = input()
        pywhatkit.sendwhatmsg(g,k,20,38)

    elif 'open google' in comm:
        talk('opening google')
        url = "https://www.google.com"
        webbrowser.open_new(url)

    elif 'play music' in comm:
        songs = ":C\\Users\\Music\\song"
        song = os.listdir(songs)
        print(song)
    elif 'send email' in comm:
        import smtplib
        gmailaddress = input("what is your gmail address? \n ")
        gmailpassword = input("what is the password for that email address? \n  ")
        mailto = input("what email address do you want to send your message to? \n ")
        msg = input("What is your message? \n ")
        mailServer = smtplib.SMTP('smtp.gmail.com', 587)
        mailServer.starttls()
        mailServer.login(gmailaddress, gmailpassword)
        mailServer.sendmail(gmailaddress, mailto, msg)
        print(" \n Sent!")
        mailServer.quit()

run_kris()






