import pyttsx3 as px

engine = px.init()

voices = engine.getProperty('voices')
# GB_HAZEL_11.0
engine.setProperty('voice', voices[1].id)


rate = engine.getProperty('rate')
engine.setProperty('rate', 180)

engine.say("Hello, my name is DarishkaAMS. I'm the Intelligent Voice Assistant in Python. Let's make miracles happen")
engine.runAndWait()
engine.stop()
