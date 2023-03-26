import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[2].id)
engine.setProperty('rate', 160)

def speaker(text):
	engine.say(text)
	engine.runAndWait()