import os
import datetime
import time
import random
from gtts import gTTS

Text = 'Initializing'

def VoiceConvert(Message):
    path = "tempvoice.mp3"
    tts = gTTS(Message)
    tts.save(path)
    print(f'Message to read : {Message}')
    ReadMessage()

def ReadMessage():
    os.popen('mpg321 tempvoice.mp3', 'w')

def Randomizer(ammount):
    RandomVar = random.randint(1,ammount)
    return(RandomVar)

def GetDateTime():
    global now
    global WeekdayToday
    now = datetime.datetime.now()
    WeekdayToday = datetime.datetime.today().weekday()
    print (f'Current date and time : {now.strftime("%Y-%m-%d %H:%M:%S")}')

while True:
    VoiceConvert(Text)
    Text = ' '
    GetDateTime()

    if now.hour == 1 and now.minute == 0:
        Text = 'Im an alert that triggers on a specific hour and minute. I will trigger at 1AM'

    if WeekdayToday == 0 and now.hour == 2 and now.minute == 0:
        Text = 'Im an alert that triggers on a specific day, hour and minute. I will trigger on Monday 2AM'

    if now.hour == 6 and now.hour == 0:
        No = Randomizer(3)
        if (No == 1):
            Text = 'Im a randomizer. random 1'
        elif (No == 2):
            Text = 'Im another randomizer. random 2'
        elif (No == 3):
            Text = 'This is my final random comment. random 3'

    ##----------------------------------------------------------------------------
    ## WeekdayToday = 0 = Monday
    ## WeekdayToday = 1 = Tuesday
    ## WeekdayToday = 2 = Wednesday
    ## WeekdayToday = 3 = Thursday
    ## WeekdayToday = 4 = Friday
    ## WeekdayToday = 5 = Saturday
    ## WeekdayToday = 6 = Sunday
        
    time.sleep(60)