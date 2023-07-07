import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

userInput = int(input("Press 1 for Text-To-Speech\nPress 2 for Speech-To-Text\n"))

if (userInput == 1):
    engine.say(input("Enter text : "))
    engine.runAndWait()

elif (userInput == 2):
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
        print("Sorry, couldn't hear you")

else:
    raise ValueError("Enter valid value")