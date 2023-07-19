# pip install pyttsx3
# pip install speechRecognition
# pip install wikipedia
# pip install requests

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import time
import smtplib
import requests
import json
from pytube import YouTube
import string
from pyautogui import hotkey

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def speak(audio):
    ''' Speaks Audio '''
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    ''' Wishes the user, according to the time '''
    hour = int(datetime.datetime.now().hour)
    if (3 <= hour < 12):
        speak("Good Morning!")
    elif (12 <= hour < 17):
        speak("Good Afternoon")
    elif (17 <= hour < 23):
        speak("Good Evening")
    else:
        speak("Good Night")

    speak("I'm Cortana, your AI assistant")
    speak("How may I help you?")

def takeCommand():
    ''' Takes microphone input, returns string output '''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said : {query}\n")
    
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def Audio():
    ''' Downloads an audio file from youtube '''
    yt = YouTube(url)
    aud = yt.streams.last().download(filename=filename)
    print("Your file is saved at", os.path.abspath(filename))
    speak(f"Your file is saved at {os.path.abspath(filename)}")

def Video():
    ''' Downloads a video file from youtube '''
    yt = YouTube(url)
    video = yt.streams
    vid = list(enumerate(video))
    video[2].download(filename=filename)
    print("Your file is saved at", os.path.abspath(filename))
    speak(f"Your file is saved at {os.path.abspath(filename)}")

if __name__ == "__main__":
    # wishMe()
    while True:
        # query = takeCommand().lower()
        query = "refresh drivers"

        # Logic for executing tasks based on query
        if "wish me" in query:
            wishMe()

        elif "who are you" in query or "about you" in query:
            speak("Hello, I am Cortana, I was created by Sahil Sonawane for assisting people for their personal uses. This is a basic version of myself, in the coming time you would be seeing an advanced version of me.")

        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "open google" in query:
            webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("google.com")

        elif "open youtube" in query:
            webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("youtube.com")
        
        elif "open get hub" in query:
            webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("github.com")
        
        elif "open drive" in query:
            webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("drive.google.com")
        
        elif "open notes" in query:
            webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("keep.google.com")
        
        elif "music" in query:
            musicDir = "C:/Users/sahil/Music/"
            songs = os.listdir(musicDir)
            randomSong = songs[random.randint(0,len(songs))]
            if (randomSong == "desktop.ini"):
                randomSong = songs[random.randint(0,len(songs))]
            os.startfile(os.path.join(musicDir, randomSong))
            print("Playing...")
            print(randomSong.removesuffix(".mp3" or ".mp4" or ".webm"))
            speak(f"Playing {randomSong.removesuffix('.mp3' or '.mp4' or '.webm')}")
            break
        
        elif "the time" in query:
            strTime = time.strftime("%I:%M %p")
            print(time.strftime("%I:%M:%S %p"))
            speak(f"Sir, the time is {strTime}")
        
        elif "date" in query:
            strDate = time.strftime("%B %d, %Y")
            print(strDate)
            speak(f"Sir, today's date is {strDate}")
        
        elif "news" in query:
            date = datetime.date.today()
            speak("What news would you like to hear?")
            news = takeCommand()
            apiKey = open("C:/API/News.txt", "r").read()
            url = f"https://newsapi.org/v2/everything?q={query}&from{date}&sortBy=publishedAt&apiKey={apiKey}"
            r=requests.get(url)
            news = json.loads(r.text)

            for article in news["articles"]:
                print(article["title"])
                print(article["description"])
                print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                speak(article["title"])

        elif "day" in query:
            strDay = time.strftime("%A")
            print(time.strftime("%A\nToday is %jth day of the year"))
            speak(f"Sir, today is {strDay}")
        
        elif "youtube download" in query:
            url = input("Enter url : ")
            downloadFormat = input("Enter format : ")
            filename = input("Enter file name : ")

            if (downloadFormat == "Video") or (downloadFormat == "video") or (downloadFormat == ".mp4") or (downloadFormat == "mp4"):
                Video()

            elif (downloadFormat == "Audio") or (downloadFormat == "audio") or (downloadFormat == ".mp3") or (downloadFormat == "mp3") or (downloadFormat == ".webm") or (downloadFormat == "webm"):
                Audio()

            else:
                raise ValueError()
        
        elif "password" in query:
            a = "".join(random.choice(string.ascii_lowercase)for i in range(10))
            b = "".join(random.choice(string.ascii_uppercase)for i in range(10))
            c = "".join(random.choice(string.digits)for i in range(10))
            d = "".join(random.choice(string.punctuation)for i in range(10))

            randomChoice = a+b+c+d

            speak("Please enter password length")
            passwordlength = int(input("Enter password length : "))

            password = "".join(random.choice(randomChoice)for i in range (passwordlength))
            print(password)
            speak("Here is your passord")

        elif "open code" in query or "vs code" in query:
            os.startfile("C:/VS Code/Code.exe")
        
        elif "open typing master" in query:
            os.startfile("C:/Users/sahil/AppData/LocalPrograms/TypingMaster/TypingMaster.exe")
        
        elif "open bash" in query:
            os.startfile("C:/Git/git-bash.exe")
        
        elif "open settings" in query:
            hotkey("win", "i")
        
        elif "refresh drivers" in query:
            hotkey("win", "ctrl", "shift", "b")

        elif ("screen shot" in query) or ("screenshot" in query):
            hotkey("win", "shift", "s")
        
        elif "open file system" in query:
            os.startfile("C:/Windows/explorer.exe")
        
        elif "open note pad" in query:
            os.startfile("C:/Windows/notepad.exe")
        
        elif "antivirus" in query:
            os.startfile("C:/Windows/System32/MRT.exe")
        
        elif "eject device" in query:
            os.startfile("C:/Windows/System32/DeviceEject.exe")
        
        elif "cmd" in query:
            os.startfile("C:/Windows/System32/cmd.exe")
        
        elif "control panel" in query:
            os.startfile("C:/Windows/System32/control.exe")
        
        elif "clean master" in query:
            os.startfile("C:/Windows/System32/cleanmgr.exe")
        
        elif "calculator" in query:
            os.startfile("C:/Windows/System32/calc.exe")
        
        elif "break" in query or "shut" in query or "shut up" in query or "shutdown" in query or "exit" in query:
            hour = int(datetime.datetime.now().hour)
            if (23 <= hour < 3):
                speak("Thank you for using me, good night")
                exit()
            else:
                speak("Thank you for using me.")
                exit()