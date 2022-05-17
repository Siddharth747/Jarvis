import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener=sr.Recognizer()
engine= pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Im Listening...")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if "jarvis" in command:
                command=command.replace("jarvis","")
    except:
        pass
    return command

def run_jarvis():
    command=take_command()
    print(command)
    if "play" in command:
        song =command.replace('play','')
        talk('playing'+ song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time=datetime.datetime.now().strftime("%I %M %p")
        talk("Current time is"+time)
    elif "search" in command:
        info = command.replace("search","")
        search = wikipedia.summary(info,1)
        print(search)
        talk(search)
    elif 'do you have a girlfriend' in command:
        talk("Madarchod Tatte kaam karle apna")
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk("Bitch say again.")

run_jarvis()