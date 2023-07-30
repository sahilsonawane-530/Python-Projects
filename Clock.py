# pip install playsound
# pip install pytz

from playsound import playsound
import time
from winsound import Beep
from datetime import datetime
from pytz import timezone, all_timezones

def Alarm():
    ''' Ring's at a specific time '''

    Hours = int(time.strftime('%H'))
    Minutes = int(time.strftime('%M'))
    Seconds = int(time.strftime('%S'))
    realTime = (f"{Hours:02d}:{Minutes:02d}:{Seconds:02d}")
    print(f"Real time is {realTime}")

    inputHours = int(input("Enter hours : "))
    inputMinutes = int(input("Enter minutes : "))
    inputSeconds = int(input("Enter seconds : "))

    alarmTime = (f"{inputHours:02d}:{inputMinutes:02d}:{inputSeconds:02d}")
    print(f"\nAlarm will ring at {alarmTime}")

    while True:
        Hours = int(time.strftime('%H'))
        Minutes = int(time.strftime('%M'))
        Seconds = int(time.strftime('%S'))
        realTime = (f"{Hours:02d}:{Minutes:02d}:{Seconds:02d}")
        if (realTime == alarmTime):
            Beep(frequency=2500, duration=1000)
            Beep(frequency=2500, duration=1000)
            Beep(frequency=2500, duration=1000)
            Beep(frequency=2500, duration=1000)
            Beep(frequency=2500, duration=1000)
            exit()

def WorldClock():
    ''' Display's World Clock '''
    date = "%B %d, %Y"
    time = "%H:%M:%S"
    timeZoneFollowed = "%Z"
    GMTcompared = "%z"
    
    # Current time in UTC
    now_utc = datetime.now(timezone('UTC'))
    
    # Convert to {input} time zone
    country = input("Enter Country : ")
    if (country == "timezones"):
        for tz in all_timezones:
            print(tz)
        country = input("Enter Country : ")
    nowTime = now_utc.astimezone(timezone(country))
    formation = f"\nDate in {country} : {date}\nTime in {country} : {time}\nTime Zone followed by {country} : {timeZoneFollowed}\n{timeZoneFollowed} compared to GMT : {GMTcompared}"
    print(nowTime.strftime(formation))

def Stopwatch():
    ''' Stopwatch '''
    hours = 0
    minutes = 0
    seconds = 0

    print("Press \"ENTER\" to start ")
    while True:
        try :
            input()
            while True:
                seconds = seconds + 1
                if seconds >= 60:
                    minutes = minutes + 1
                    seconds = 0

                if minutes >= 60:
                    hours = hours + 1
                    minutes = 0
                    seconds = 1
                    Beep(frequency=2500, duration=1000)
                
                timeTook = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
                print(timeTook, end="\r")
                time.sleep(1)

        except KeyboardInterrupt:
            print(f"Time took : {timeTook}")
            exit()

def CountdownTimer():
    ''' Ring's once the given time ends '''
    
    timeElapsed = 0
    hours = int(input("Hours to wait : "))
    minutes = int(input("Minutes to wait : "))
    seconds = int(input("Seconds to wait : "))
    totalSeconds = (hours * 3600) + (minutes * 60) + seconds

    while (timeElapsed < totalSeconds):
        time.sleep(1)
        timeElapsed = timeElapsed + 1

        timeLeft = totalSeconds - timeElapsed
        hoursLeft = timeLeft // 3600
        minutesLeft = (timeLeft % 3600) // 60
        secondsLeft = timeLeft % 60

        print(f"{hoursLeft:02d}:{minutesLeft:02d}:{secondsLeft:02d}", end="\r")
    
    Beep(frequency=2500, duration=5000)

userInput = int(input("Press 1 for Alarm\nPress 2 for World Clock\nPress 3 for Stopwatch\nPress 4 for Countdown Timer\n"))

if (userInput == 1):
    Alarm()

elif (userInput == 2):
    WorldClock()

elif (userInput == 3):
    Stopwatch()

elif (userInput == 4):
    CountdownTimer()

else:
    raise ValueError("Enter valid value")