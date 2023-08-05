import speech_recognition as sr
import pyttsx3
import os
import datetime
import pywhatkit
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("hi i am jarvis")
engine.say("what can i do for you boss")
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    if "play" in command:
        song = command.replace("play", "")
        talk("playing " + song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk(time)

    elif "search" in command:
        query = command.replace("search", "")
        info = wikipedia.summary(query)
        print(info)
        talk(info)
    elif "whatsapp" in command:
        talk("opening WhatsApp Web")
        os.startfile("C:\\Users\\kaila\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    elif "google" in command:
        talk("opening Google")
        os.system('start "" "https://www.google.com/"')
    elif "code" in command:
        talk("opening vscode")
        os.startfile("C:\\Users\\kaila\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
    else:
        talk("say the command again")


while True:
    run_alexa()
