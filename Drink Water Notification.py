# pip install plyer
# pip install pyttsx3

from plyer import notification
import pyttsx3
import time

engine=pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

notification.notify(
title = "Reminder",
message = ("Drink 1 glass of water"),
timeout = 10
)
while True:
    engine.say("Please Drink Water")
    engine.runAndWait()
    time.sleep(30*60)