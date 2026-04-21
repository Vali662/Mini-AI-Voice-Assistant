import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import os
import requests
import psutil
import pyautogui
from features.brightness import set_low_brightness, set_high_brightness


engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        command = command.lower()
        print("You:", command)
    except:
        speak("Say that again please")
        return ""
    return command

# Weather
def get_weather(city):
    api_key = "YOUR_API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        data = requests.get(url).json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        speak(f"{city} temperature is {temp}°C with {desc}")
    except:
        speak("Weather not available")

# Battery
def battery_status():
    battery = psutil.sensors_battery()
    percent = battery.percent
    speak(f"Battery is at {percent} percent")

# Screenshot
def take_screenshot():
    img = pyautogui.screenshot()
    img.save("screenshot.png")
    speak("Screenshot taken")

def run_assistant():
    command = take_command()

    # Time & Date
    if "time" in command:
        speak(datetime.datetime.now().strftime('%I:%M %p'))

    elif "date" in command:
        speak(datetime.datetime.now().strftime('%d %B %Y'))

    # Wikipedia
    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, 1)
        speak(info)

    # YouTube
    elif "play" in command:
        song = command.replace("play", "")
        speak("Playing " + song)
        pywhatkit.playonyt(song)

    # Google Search
    elif "search" in command:
        query = command.replace("search", "")
        pywhatkit.search(query)
        speak("Here is what I found")

    # Open Apps
    elif "open youtube" in command:
        os.system("start https://youtube.com")

    elif "open google" in command:
        os.system("start https://google.com")

    elif "open notepad" in command:
        os.system("notepad")

    elif "open whatsapp" in command:
        os.system("start https://wa.me/qr/VTVBFCY6VONQM1")

    elif "open settings" in command:
        os.system("start ms-settings:network-wifi")

    elif "open chrome" in command:
        os.system("start https://www.google.com")

    # Weather
    elif "weather" in command:
        speak("Tell city name")
        city = take_command()
        get_weather(city)

    # System Info
    elif "battery" in command:
        battery_status()

    # Screenshot
    elif "screenshot" in command:
        take_screenshot()

    # Volume control
    elif "volume up" in command:
        pyautogui.press("volumeup")

    elif "volume down" in command:
        pyautogui.press("volumedown")

    elif "mute" in command:
        pyautogui.press("volumemute")

    # Screen brightness control
    elif "low brightness" in command:
       speak(set_low_brightness())

    elif "high brightness" in command:
       speak(set_high_brightness())

    # Exit
    elif "exit" in command or "stop" in command:
        speak("Goodbye")
        exit()

    else:
        speak("I didn't understand")

# Start
speak("Hello Boss, I am your AI assistant Tell me how can i help you?")
while True:
    run_assistant()




