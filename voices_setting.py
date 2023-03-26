import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 170)
i = 0
for voice in voices:
    print(voice, voice.id)
    engine.setProperty('voice', voice.id)
    engine.say(f"это тест моего голоса номер {i} на русском")
    engine.say("If you only hear this, the voice only supports English")
    engine.runAndWait()
    engine.stop()
    i += 1
input()