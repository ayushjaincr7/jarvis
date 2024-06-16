import os
from decouple import config
from datetime import datetime
import speech_recognition as sr
from random import choice
from utils import opening_text


USERNAME = config('USER')
BOTNAME = config('BOTNAME')

# Define the function for text-to-speech conversion
def speak(text):
    os.system(f"osascript -e 'say \"{text}\"'")


def greet_user():
    hour = datetime.now().hour
    if (hour>=6) and (hour<12):
        speak(f'Good Morning {USERNAME}')
    elif (hour>=12) and (hour<16):
        speak(f'Good afternoon {USERNAME}')
    elif (hour>=16) and (hour<19):
        speak(f'Good Evening {USERNAME}')
    speak(f"I am {BOTNAME}. How may I assist you?")


def take_user_input():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening.....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing....')
        query = r.recognize_google(audio, language="en-in")
        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()
    except Exception:
        speak('Sorry, I could not understand. Could you please say that again?')
        query = 'None'
    return query
text = take_user_input()