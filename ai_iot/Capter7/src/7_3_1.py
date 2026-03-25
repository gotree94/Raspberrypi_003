from gpiozero import Button
import subprocess
import time
import os
from openai import OpenAI

#client = OpenAI(api_key="sk-proj-*********************")

BUTTON_PIN = 5
WAV_PATH = "button_stt.wav"

button = Button(BUTTON_PIN, pull_up=False, bounce_time=0.1)

record_proc = None

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

    print("STT start...")

    with open(WAV_PATH, "rb") as f:
        result = client.audio.transcriptions.create(
            model="gpt-4o-mini-transcribe",
            file=f,
            response_format="json"
        )

    print("STT result:")
    print(result.text)

button.when_pressed = start_record
button.when_released = stop_record

print("Press and hold the button to record, release to STT (Ctrl+C to exit)")

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Exit")
