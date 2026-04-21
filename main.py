import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import random
import psutil
import pyautogui
import pywhatkit
from features.brightness import set_low_brightness, set_high_brightness

# ---------- INIT ----------
engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# ---------- LISTEN ----------
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        except:
            return ""

    try:
        command = r.recognize_google(audio, language='en-IN')
        command = command.lower()
        print("You:", command)
    except:
        return ""

    return command

# ---------- DATA ----------
tasks = []
jokes = [
    "Why do programmers hate bugs? Because they take too much time!",
    "Python is easy, that's why I exist"
]

# ---------- MAIN ----------
def run_assistant():
    command = take_command()

    # TIME
    if "time" in command:
        speak(datetime.datetime.now().strftime('%I:%M %p'))

    # DATE
    elif "date" in command:
        speak(datetime.datetime.now().strftime('%d %B %Y'))

    # YouTube
    elif "play" in command:
        movie = command.replace("play","")
        song = command.replace("play", "")
        speak("playing " + movie)
        speak("Playing " + song)
        pywhatkit.playonyt(song)
       # pywhatkit.playonyt(movie)


    # OPEN WEBSITES
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")

    elif "open google" in command:
        webbrowser.open("https://google.com")

    elif "open instagram" in command:
        webbrowser.open("https://instagram.com")

    elif "open notepad" in command:
        os.system("notepad")

    elif "open whatsapp" in command:
        os.system("start https://wa.me/qr/VTVBFCY6VONQM1")

    elif "open settings" in command:
        os.system("start ms-settings:network-wifi")

    elif "open chrome" in command:
        os.system("start https://www.google.com")


    # SEARCH
    elif "search" in command:
        speak("What should I search?")
        query = take_command()
        webbrowser.open(f"https://www.google.com/search?q={query}")

    # TO-DO LIST
    elif "add task" in command:
        speak("What is the task?")
        task = take_command()
        tasks.append(task)
        speak("Task added")

    elif "show tasks" in command:
        if tasks:
            speak("Your tasks are")
            for t in tasks:
                speak(t)
        else:
            speak("No tasks found")

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


    # NOTES
    elif "write note" in command:
        speak("What should I write?")
        note = take_command()
        with open("notes.txt", "a") as f:
            f.write(note + "\n")
        speak("Note saved")

    # JOKE
    elif "tell joke" in command:
        speak(random.choice(jokes))

    # BATTERY
    elif "battery" in command:
        battery = psutil.sensors_battery()
        speak(f"Battery is {battery.percent} percent")

    # SIMPLE SYSTEM CONTROL
    elif "shutdown" in command:
        speak("Shutting down")
        os.system("shutdown /s /t 5")

    elif "restart" in command:
        speak("Restarting")
        os.system("shutdown /r /t 5")

    # EXIT
    elif "exit" in command or "stop" in command:
        speak("Goodbye")
        exit()

    else:
        if command != "":
            speak("I didn't understand")

    

# ---------- GREETING ----------
hour = datetime.datetime.now().hour
if hour < 12:
    speak("Good morning boss, I am your AI assistant")
elif hour < 18:
    speak("Good afternoon boss, I am your AI assistant")
else:
    speak("Good evening boss, I am your AI assistant")

#speak("Hello, I am your AI assistant")

# ---------- START ----------
while True:
    run_assistant()