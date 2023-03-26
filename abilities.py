import voice
import webbrowser
import sys
import requests
from apikeys import WEATHER_API_TOKEN
import subprocess

def browser():
    webbrowser.open('https://www.youtube.com', new=2)

def open():
    try:
        subprocess.Popen('C:/Program Files/paint.net/PaintDotNet.exe')
    except:
        voice.speaker('Путь к файлу не найден, проверьте, правильный ли он')

def weather():
    try:
        params = {'q': 'Omsk', 'units': 'metric', 'lang': 'ru', 'appid': WEATHER_API_TOKEN}
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=params)
        if not response:
            raise
        w = response.json()
        r = round(w['main']['temp'])
        g = "градуса" if r in range(2,5) else "градусов" if r in range(6,10) else "градус"
        voice.speaker(f"На улице {w['weather'][0]['description']} {r} {g}")

    except:

        voice.speaker('Произошла ошибка при попытке запроса к ресурсу API, проверь код')

def botOff():
    sys.exit()

def passive():
    pass