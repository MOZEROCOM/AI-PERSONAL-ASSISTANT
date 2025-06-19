#timeDate.py
import datetime
from speak import speak

def time(command):
    if "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")

    elif "date" in command or"today"in command or "day" in command:
        today = datetime.date.today().strftime("%A, %B %d, %Y")
        speak(f"Today is {today}")

   