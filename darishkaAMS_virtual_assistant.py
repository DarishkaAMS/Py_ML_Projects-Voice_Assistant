import pyttsx3 as px

engine = px.init()

voices = engine.getProperty('voices')

# GB_HAZEL_11.0
engine.setProperty('voice', voices[1].id)

engine.say("Hello, my name is DarishkaAMS. Let's make miracles happen")
engine.runAndWait()
engine.stop()
