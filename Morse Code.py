import pyttsx3

def speak(audio):
    ''' Speaks Audio '''
    engine.say(audio)
    engine.runAndWait()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

a = input("Enter character(s) : ")

if (a == "A" or a == "a"):
    print("• — ALFA")
    speak("Dik - Dah")

elif (a == "B") or (a=="b"):
    print("— • • • BRAVO")
    speak("Dah - Dik - Dik - Dik")

elif (a == "C") or (a=="c"):
    print("— • — • CHARLIE")
    speak("Dah - Dik - Dah - Dik")

elif (a == "D") or (a=="d"):
    print("— • • DELTA")
    speak("Dah - Dik - Dik")

elif (a == "E") or (a=="e"):
    print("• ECHO")
    speak("Dik")

elif (a == "F") or (a=="f"):
    print("• • — • FOXTROT")
    speak("Dik - Dik - Dah - Dik")

elif (a == "G") or (a=="g"):
    print("— — • GOLF")
    speak("Dah - Dah - Dik")

elif (a == "H") or (a=="h"):
    print("• • • • HOTEL")
    speak("Dik - Dik - Dik - Dik")

elif (a == "I") or (a=="i"):
    print("• • INDIA")
    speak("Dik - Dik")

elif (a == "J") or (a=="j"):
    print("• — — — JULIET")
    speak("Dik - Dah - Dah - Dah")

elif (a == "K") or (a=="k"):
    print("— • — KILO")
    speak("Dah - Dik - Dah")

elif (a == "L") or (a=="l"):
    print("• — • • LIMA")
    speak("Dik - Dah - Dik - Dik")

elif (a == "M") or (a=="m"):
    print("— — MIKE")
    speak("Dah - Dah")

elif (a == "N") or (a=="n"):
    print("— • NOVEMBER")
    speak("Dah - Dik")

elif (a == "O") or (a=="o"):
    print("— — — OSCAR")
    speak("Dah - Dah - Dah")

elif (a == "P") or (a=="p"):
    print("— • • • PAPA")
    speak("Dah - Dik - Dik - Dik")

elif (a == "Q") or (a=="q"):
    print("— — • — QUEBEC")
    speak("Dah - Dah - Dik - Dah")

elif (a == "R") or (a=="r"):
    print("• — • ROMEO")
    speak("Dik - Dah - Dik")

elif (a == "S") or (a=="s"):
    print("• • • SIERRA")
    speak("Dik - Dik - Dik")

elif (a == "T") or (a=="t"):
    print("— TANGO")
    speak("Dah")

elif (a == "U") or (a=="u"):
    print("• • — UNIFORM")
    speak("Dik - Dik - Dah")

elif (a == "V") or (a=="v"):
    print("• • • — VICTOR")
    speak("Dik - Dik - Dik - Dah")

elif (a == "W") or (a=="w"):
    print("• — — WHISKEY")
    speak("Dik - Dah - Dah ")

elif (a == "X") or (a=="x"):
    print("— • • — XRAY")
    speak("Dah - Dik - Dik - Dah")

elif (a == "Y") or (a=="y"):
    print("— • — —")
    speak("Dah - Dik - Dah - Dah")

elif (a == "Z") or (a=="z"):
    print("— — • • ZULU")
    speak("Dah - Dah - Dik - Dik")

elif (a == "0") or (a=="Zero") or (a == "zero"):
    print("— — — — — BRAVO")
    speak("Dah - Dah - Dah - Dah - Dah")

elif (a == "1") or (a=="One") or (a == "one"):
    print("• — — — — ONE")
    speak("Dah - Dik - Dik - Dik")

elif (a == "2") or (a=="Two") or (a == "two"):
    print("• • — — — TWO")
    speak("Dik - Dik - Dah - Dah - Dah")

elif (a == "3") or (a=="Three") or (a == "three"):
    print("• • • — — THREE")
    speak("Dik - Dik - Dik - Dah - Dah")

elif (a == "4") or (a=="Four") or (a == "four"):
    print("• • • • — FOUR")
    speak("Dik - Dik - Dik - Dik - Dah")

elif (a == "5") or (a=="Five") or (a == "five"):
    print("• • • • • FIVE")
    speak("Dik - Dik - Dik - Dik - Dik")

elif (a == "6") or (a=="Six") or (a == "six"):
    print("— • • • • SIX")
    speak("Dah - Dik - Dik - Dik - Dik")

elif (a == "7") or (a=="Seven") or (a == "seven"):
    print("— — • • • SEVEN")
    speak("Dah - Dah - Dik - Dik - Dik")

elif (a == "8") or (a=="Eight") or (a == "eight"):
    print("— — — • • EIGHT")
    speak("Dah - Dah - Dah - Dik - Dik")

elif (a == "9") or (a=="Nine"):
    print("— — — — • NINE")
    speak("Dah - Dah - Dah - Dah - Dik")

else:
    raise ValueError("Enter valid value")