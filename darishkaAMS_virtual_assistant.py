import datetime
from email.message import EmailMessage
import pyttsx3 as px
import speech_recognition as sr


engine = px.init()

# Assistant and User setup
user = "Daryna Nikolaienko"
assistant = "DarishkaAMS"
voices = engine.getProperty('voices')
# GB_HAZEL_11.0
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)

# Start Greeting
engine.say(f"Hello, my name is {assistant}. I'm the Intelligent Voice Assistant in Python. Let's make miracles happen")
engine.runAndWait()
engine.stop()

# recognizer = sr.Recognizer()
# with sr.Microphone() as source:
#     recognizer.energy_threshold = 10_000
#     print("listen")
#     audio = recognizer.listen(source)
#     text = recognizer.recognize_google(audio)
#     print(text)


# General Output
def output(out):
    # print(out)
    engine.say(out)
    engine.runAndWait()
    engine.stop()


# Time Greetings
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


# Email Sending
def send_email():
    email_list = {
        "test": "honeydummyams@gmail.com"
    }
    try:
        email = EmailMessage()
        output("Whom should I send this e-mail?")
        name = inputCommand().lower()
        email["To"] = email_list[name]
        output("How about the e-mail title?")
        email["Subject"] = inputCommand()
        email["From"] = email_sender
        output("What should i Say?")
        email.set_content(inputCommand())
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(email_sender, password)
        s.send_message(email)
        s.close()
        output("Email has benn sent")
    except Exception as e:
        print(e)
        output("I can't send the e-mail. Sorry...")