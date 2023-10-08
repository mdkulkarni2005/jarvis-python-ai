import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import os
import wikipedia
import pyautogui
import keyboard



# Enginer of jarvis
Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voices', voices[0].id)


# all jarvis function
def Speak(audio):
    print("  ")
    Assistant.say(audio)
    print(f": {audio}")
    Assistant.runAndWait()

def takeCommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recongning...")
            query = command.recognize_google(audio, language='en-in')
            print(f"You Said :  {query}")

        except Exception as Error: 
            return "None"
        
        return query.lower()

def TaksExe():

    Speak("Hello, I am Jarvis")
    Speak("How can I Help you")

    
    def YoutubeAuto():
        Speak("What Your Command ?")
        comm = takeCommand()

        if 'pause' in query:
            keyboard.press('space bar')

        elif 'restart' in query:
            keyboard.press('0')
            
        elif 'mute' in query:
            keyboard.press('m')

        elif 'skip' in query:
            keyboard.press('l')

        elif 'back' in query:
            keyboard.press('j')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'film mode' in query:
            keyboard.press('t')

        elif 'miniplayer' in query:
            keyboard.press('i')

        elif 'volume up' in query:
            keyboard.press('up arrow')

        elif 'volume down' in query:
            keyboard.press('down arrow')

        elif 'search' in query:
            keyboard.press('/')

        Speak("Done sir")
    
    def ChromeAuto():
        Speak("Chrome Automation started")

        command = takeCommand()

        if 'close this tab' in command:
            keyboard.press_and_release('ctrl + w')

        if 'open new tab' in command:
            keyboard.press_and_release('ctrl + t')

        if 'open new window' in command:
            keyboard.press_and_release('ctrl + n')

        if 'search on chrome' in command:
            keyboard.press_and_release('/')

        if 'history' in command:
            keyboard.press_and_release('ctrl + h')

        if 'change the window' in command:
            keyboard.press_and_release('alt + tab')


    while True:

        query = takeCommand()

        if'hello' in query:
            Speak("Hello Sir, I am Jarvis .")
            Speak("How may I Help You")

        elif 'you need a break' in query:
            Speak("OK sir you can call me anytime")
            Speak("Just Say Wake up Jarvis")
            break

        elif 'youtube search' in query:
            query = query.replace("jarvis", "")
            query = query.replace("youtube search", "")
            Speak("OK Sir, This is what is found for you Search")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            Speak("Done sir")

        elif 'google search' in query:
            query = query.replace("jarvis", "")
            query = query.replace("google search", "")
            Speak("OK Sir, This is what is found for you Search")
            pywhatkit.search(query)
            web = '' + query
            Speak("Done sir")

        elif 'websit' in query:
            Speak("Ok sir, Launching...")
            query = query.replace("jarvis", "")
            query = query.replace("website", "")
            query = query.replace(" ", "")
            web1 = query.replace("open", "")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            Speak("Launched!")
            
        elif 'wikipedia' in query:
            Speak("Searching Wikipedia...")
            query = query.replace("jarvis", "")
            query = query.replace("wikipedia", "")
            wiki = wikipedia.summary(query,2)
            Speak(f"According To Wikipedia : {wiki}")

        elif "open" in query:
            from Dictapp import openappweb
            openappweb(query)

        elif "close" in query:
            from Dictapp import closeappweb
            closeappweb(query)

        elif 'pause' in query:
            keyboard.press('space bar')

        elif 'restart' in query:
            keyboard.press('0')
            
        elif 'mute' in query:
            keyboard.press('m')

        elif 'skip' in query:
            keyboard.press('l')

        elif 'back' in query:
            keyboard.press('j')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'film mode' in query:
            keyboard.press('t')

        elif 'small' in query:
            keyboard.press('i')

        elif 'volume up' in query:
            keyboard.press('up arrow')

        elif 'volume down' in query:
            keyboard.press('down arrow')

        elif 'search' in query:
            keyboard.press('/')

        elif 'youtube tool' in query:
            YoutubeAuto()

        elif 'close this tab' in query:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')

        elif 'search on chrome' in query:
            keyboard.press_and_release('/')

        elif 'history' in query:
            keyboard.press_and_release('ctrl + h')

        elif 'change the window' in query:
            keyboard.press_and_release('alt + tab')
    
        elif "whatsapp" in query:
            from Whatsapp import sendMessage
            sendMessage()

TaksExe()