from gpiozero import Button
from openai import OpenAI
import subprocess
import pygame
import tempfile
import time
import os

#client = OpenAI(api_key="sk-proj-****************")

BUTTON_PIN = 5
WAV_PATH = "question.wav"

button = Button(BUTTON_PIN, pull_up=False, bounce_time=0.1)

record_proc = None

pygame.init()
pygame.mixer.init()

def start_record():
    global record_proc

    if record_proc is not None:
        return

    print("Button pressed")
    print("Start recording...")

    if os.path.exists(WAV_PATH):
        os.remove(WAV_PATH)

    cmd = [
        "arecord",
        "-f", "S16_LE",
        "-c", "1",
        "-r", "16000",
        WAV_PATH
    ]

    record_proc = subprocess.Popen(cmd)

def stop_record():
    global record_proc

    print("Button released")
    print("Stop recording")

    if record_proc is None:
        return

    record_proc.terminate()
    record_proc.wait()
    record_proc = None

    if not os.path.exists(WAV_PATH):
        print("No recorded file")
        return

    print("Transcribing...")

    with open(WAV_PATH, "rb") as f:
        result = client.audio.transcriptions.create(
            model="gpt-4o-mini-transcribe",
            file=f,
            response_format="json"
        )

    text = result.text
    print("You said:")
    print(text)

    print("Asking ChatGPT...")

    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": text}
        ]
    )

    answer = resp.choices[0].message.content
    print("Assistant:")
    print(answer)

    print("Generating TTS...")

    speech = client.audio.speech.create(
        model="gpt-4o-mini-tts",
        voice="alloy",
        input=answer,
        response_format="wav"
    )

    audio_bytes = speech.read()

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        f.write(audio_bytes)
        wav_path = f.name

    pygame.mixer.music.load(wav_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    os.remove(wav_path)

button.when_pressed = start_record
button.when_released = stop_record

print("Hold button to record, release for voice answer (Ctrl+C to exit)")

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Exit")
    pygame.mixer.quit()
