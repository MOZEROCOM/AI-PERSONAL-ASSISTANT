
import json
import os
from speak import speak
from listen import listen

MEMORY_FILE = "memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {"custom_commands": {}}
    try:
        with open(MEMORY_FILE, "r") as f:
            data = json.load(f)
            if not isinstance(data, dict):
                return {"custom_commands": {}}
            if "custom_commands" not in data:
                data["custom_commands"] = {}
            return data
    except json.JSONDecodeError:
        return {"custom_commands": {}}

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)

def remember(key, value):
    memory = load_memory()
    memory[key] = value
    save_memory(memory)
    print(f"[DEBUG] Saved {key} = {value}")

def recall(key):
    return load_memory().get(key, None)

def get_valid_input(prompt, max_attempts=3):
    for attempt in range(max_attempts):
        speak(prompt)
        response = listen()
        if response and response.strip():
            return response.strip()
        speak(f"I didn't catch that. Please try again attempt {attempt+1}")
    speak("Okay, let's skip that.")
    return None

def memory(command):
    if "what do you remember" in command or "list memory" in command:
        memory_data = load_memory()
        for key, value in memory_data.items():
            if key != "custom_commands":
                speak(f"{key} is {value}")

    elif "list commands" in command:
        memory_data = load_memory()
        cmds = memory_data.get("custom_commands", {})
        if cmds:
            for trigger in cmds:
                speak(f"Command: {trigger}")
        else:
            speak("I haven't learned any custom commands yet.")

    elif "remember" in command:
        data = get_valid_input("What should I remember?")
        if not data:
            return
        key = get_valid_input("What should I call it?")
        if not key:
            return
        remember(key, data)
        speak(f"I will remember {data} as {key}.")

    elif "learn" in command:
        trigger = get_valid_input("What should I learn?")
        if not trigger:
            return        
        response = get_valid_input("What should I say when I hear that?")
        memory_data = load_memory()
        memory_data["custom_commands"] = memory_data.get("custom_commands", {})
        if trigger in memory_data["custom_commands"]:
            speak("I already know that. Want me to update it?")
            confirmation = listen()
            if "yes" not in confirmation:
                speak("Okay, I kept the original.")
                return
        memory_data["custom_commands"][trigger] = response
        save_memory(memory_data)
        speak("Got it!")

    elif "recall" in command or "what is" in command:
        key = (command.replace("what is my", "")
                     .replace("recall my", "")
                     .replace("recall", "")
                     .replace("what is", "")
                     .strip())
        if not key:
            key = get_valid_input("What should I recall?")
            if not key:
                return
        value = recall(key)
        if value:
            speak(f"{key} is {value}")
        else:
            speak(f"I don't remember anything about {key}.")

    elif "forget" in command:
        key = get_valid_input("What should I forget?")
        memory_data = load_memory()
        if key in memory_data:
            del memory_data[key]
            save_memory(memory_data)
            speak(f"I've forgotten {key}.")
        else:
            speak("I don't remember that.")

    # Handle custom command triggers
    memory_data = load_memory()
    custom = memory_data.get("custom_commands", {})
    for trigger, response in custom.items():
        if command.strip().lower() == trigger.strip().lower():
            speak(response)
            break
