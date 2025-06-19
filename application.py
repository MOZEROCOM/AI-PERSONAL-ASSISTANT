#application.py
import webbrowser   #imports the webbrowser library
from speak import speak     #imports the speak() function from speak.py

def appOpen(command):
    if "open youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube for you.")

    elif "open google" in command:
        webbrowser.open("https://google.com")
        speak("Opening google for you.")

    elif"open instagram" in command:
        webbrowser.open("https://instagram.com")
        speak("opening instagram for you.")
    
    elif"open facebook"in command:
        webbrowser.open("https://www.facebook.com")
        speak("opening facebook for you.")
    
    elif"open github"in command:
        webbrowser.open("https://github.com")
        speak("opening github for you.")