# main.py
from geometry import geometry
from timeDate import time
from memory import memory
from speak import speak
from application import appOpen
from mathMode import mathMode
from listen import listen

def respond(command):
    print(f"I Heard: {command}")

    if "hello" in command:
        speak("Hey Mozes. How can I assist you today?")
    

    elif "stop" in command or "exit" in command:
        speak("Are you sure you want me to shut down?")
        confirmation = listen()
        if "yes" in confirmation:
            speak("Goodbye Mozes.")
            exit()
        else:
            speak("Alright, staying on.")
    
    elif "thank you" in command:
        speak("you are welcome, thats what am made for.")


    elif "time" in command or "date" in command:        
        time(command)
    
    elif ["open youtube","open google","open facebook","open github","open instagram"] in command:
        appOpen(command)    
    

    elif ["what do you remember","list memory","list command","remember","learn", "recall " ,"forget"] in command:
         memory(command)

    elif "math mode" in command:
        mathMode()

    elif "geometry"in command:
        geometry()
    else:
        memory(command)

WAKE_WORD = "hello"
active = False

while True:
    command = listen()
    
    if WAKE_WORD in command:
        active = True
        speak("Yes Mozes, I'm listening.")
        # process remaining part of command if it exists
        parts = command.split(WAKE_WORD, 1)
        remaining = parts[1].strip()
        if remaining:
            respond(remaining)
        continue

    if active:
        if "stop listening" in command or "goodbye" in command:
            speak("Okay Mozes, I’ll wait silently.")
            active = False
        else:
            respond(command)
