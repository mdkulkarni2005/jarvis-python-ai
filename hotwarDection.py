import os
import speech_recognition as sr


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
    

while True:
    wake_Up = takeCommand()

    if 'wake up' in wake_Up:
        os.startfile('G:\\programming data\\JARVIS\\jarvis.py')

    else:
        print("nothing")