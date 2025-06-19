# MozesAI Assistant

MozesAI is a voice-activated personal assistant that works both **online** and **offline**, powered by OpenAI's Whisper and Google Speech Recognition.

## 🎯 Features

- 🔊 Voice recognition with Whisper (offline) or Google Speech API (online)
- 🧠 Memory system with JSON storage
- 🧮 Math mode and geometry calculations
- 📅 Time and date response
- 🗂️ Custom command learning
- 📡 Auto-switch between offline and online speech engines
- 🤫 Auto-stop listening on silence
- 🌐 Opens Google and YouTube by voice

## 📁 File Structure

| File           | Purpose                              |
|----------------|--------------------------------------|
| `main.py`      | Main controller and command handler  |
| `listen.py`    | Hybrid voice recognizer (Whisper + Google) |
| `speak.py`     | Text-to-speech using pyttsx3         |
| `memory.py`    | Learn, remember, recall, forget      |
| `geometry.py`  | Area, perimeter, volume calculations |
| `mathMode.py`  | Math operations, trig, log           |
| `timeDate.py`  | Time and date functions              |
| `application.py`| Opens apps like Google and YouTube  |
| `memory.json`  | Persistent memory file               |

## 📦 Installation

```bash
pip install -r requirements.txt
```

> 🔧 Also install [FFmpeg](https://ffmpeg.org/download.html) and add it to your system PATH.

## 🚀 How to Run

```bash
python main.py
```

Use your voice to trigger commands like:
- "Hello" (say this first so as to do any command)
- “Open Google”
- “Math mode”
- “Geometry”
- “Learn”
- “What is the time”
- “Good night” (custom command)

## 🛠 System Requirements

- Python 3.10+
- Mic input and speakers
- Works offline once Whisper model is downloaded

## 🧠 Future Ideas

- GUI version with Tkinter
- Reminders/alarms
- Email and file management
- Wake word detector

Made with ❤️ by Moses.
