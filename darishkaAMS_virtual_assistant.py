import datetime
import pyttsx3 as px
# import speech_recognition as sr
import time

engine = px.init()

voices = engine.getProperty('voices')
# GB_HAZEL_11.0
engine.setProperty('voice', voices[1].id)


rate = engine.getProperty('rate')
engine.setProperty('rate', 180)


engine.say("Hello, my name is DarishkaAMS. I'm the Intelligent Voice Assistant in Python. Let's make miracles happen")
engine.runAndWait()
engine.stop()

# recognizer = sr.Recognizer()
# with sr.Microphone() as source:
#     recognizer.energy_threshold = 10_000
#     print("listen")
#     audio = recognizer.listen(source)
#     text = recognizer.recognize_google(audio)
#     print(text)


def output(out):
    # print(out)
    engine.say(out)
    engine.runAndWait()
    engine.stop()

user = "DarishkaAMS"


def greet():
    hour = datetime.datetime.now().hour
    if(hour >= 6) and (hour < 12):
        output(f"Good Morning {user}")
    elif(hour >= 12) and (hour < 18):
        output(f"Good afternoon {user}")
    elif(hour >= 18) and (hour < 21):
        output(f"Good Evening {user}")
    output("How may I assist you?")


greet()
