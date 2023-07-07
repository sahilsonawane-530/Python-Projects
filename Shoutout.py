# pip install pyttsx3

import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

names = ["Sahil Sonawane", "Tushar Sonawane", "Anuradha Sonawane", "Manish Sonawane"]

for i in names:
    engine.say(f"Shoutout to {i}")
    print(f"Shoutout to {i}")
    engine.runAndWait()