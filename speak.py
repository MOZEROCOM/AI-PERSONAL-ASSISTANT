# speak.py
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 200)  # Speed of voice
def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()
