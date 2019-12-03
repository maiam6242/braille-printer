import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 130)
engine.setProperty('voice', voices[15].id)
engine.say("hello, friends!")
engine.runAndWait()