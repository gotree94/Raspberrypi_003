from gpiozero import Button
import subprocess
import time
import pygame
import os

BUTTON_PIN = 5
WAV_PATH = "record.wav"

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

    if os.path.exists(WAV_PATH):
        full_path = os.path.abspath(WAV_PATH)
        size = os.path.getsize(WAV_PATH)
        print(f"File saved: {full_path} ({size} bytes)")

        print("Playing audio...")
        pygame.mixer.music.load(WAV_PATH)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        print("Playback finished")

    else:
        print("No recorded file")

button.when_pressed = start_record
button.when_released = stop_record

print("Press and hold the button to record, release to play (Ctrl+C to exit)")

try:
    while True:
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Exit")
    pygame.mixer.quit()
