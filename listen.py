
import os
import socket
import whisper
import speech_recognition as sr
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import tempfile
from speak import speak

# Ensure FFmpeg path is available
os.environ["PATH"] += os.pathsep + "C:/ffmpeg/bin"

model = whisper.load_model("base") #for offline
recognizer = sr.Recognizer()    #for online

# checks for availability of internet connection 
def is_connected():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=2) 
        return True
    except OSError:
        return False


# records your audio
def record_audio(fs=16000, silence_threshold=1000, silence_duration=3.5, max_duration=15):
    speak("Listening...")
    print("Recording with auto-stop on silence...")

    block_size = int(fs * 0.5)  # 0.5 seconds
    silence_blocks = int(silence_duration / 0.5)
    silent_count = 0
    total_blocks = int(max_duration / 0.5)
    recording = []

    stream = sd.InputStream(samplerate=fs, channels=1, dtype='int16', blocksize=block_size)
    with stream:
        for _ in range(total_blocks):
            block, _ = stream.read(block_size)
            recording.append(block)
            volume = np.abs(block).mean()
            print(f"[DEBUG] Volume: {volume:.2f}")

            if volume < silence_threshold:
                silent_count += 1
                if silent_count >= silence_blocks:
                    print("Silence detected. Stopping early.")
                    break
            else:
                silent_count = 0

    audio = np.concatenate(recording, axis=0)
    return audio, fs

def listen():
    if is_connected():
        try:
            with sr.Microphone() as source:
                print("Listening (Google)...")
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio)
                print(f"You said (Google): {command}")
                return command.lower()
        except sr.UnknownValueError:
            speak("I didn’t catch that.")
        except sr.RequestError:
            speak("Google Speech is not available. Switching to offline mode.")

    # Whisper fallback
    audio, fs = record_audio()
    if audio is None or len(audio) == 0:
        speak("No audio detected.")
        return ""

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        wav.write(f.name, fs, audio)
        print("Transcribing with Whisper...")
        result = model.transcribe(f.name)
        text = result["text"].strip()
        print(f"You said (Whisper): {text}")
        return text.lower()
