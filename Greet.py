# pip install pyttsx3

from time import strftime
import pyttsx3

Time = strftime('%H:%M:%S')
Hours = int(strftime('%H'))
Minutes = int(strftime('%M'))
Seconds = int(strftime('%S'))

print(Time)
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

if (3 <= Hours < 12):
    print("Good Morning, Sahil Sonawane")
    engine.say("Good Morning, Sahil Sonawane")
elif (12 <= Hours < 17):
    print("Good Afternoon, Sahil Sonawane")
    engine.say("Good Afternoon, Sahil Sonawane")
elif (17 <= Hours < 23):
    print("Good Evening, Sahil Sonawane")
    engine.say("Good Evening, Sahil Sonawane")
else:
    print("Good Night, Sahil Sonawane")
    engine.say("Good Night, Sahil Sonawane")

engine.runAndWait()