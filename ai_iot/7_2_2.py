from gpiozero import Button
import subprocess
import time
import os

BUTTON_PIN = 5
WAV_PATH = "record.wav"

button = Button(BUTTON_PIN, pull_up=False, bounce_time=0.1)

record_proc = None

def start_record():
    global record_proc

    if record_proc is not None:
        return  # 이미 녹음 중이면 무시

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
        return  # 녹음 중이 아니면 무시

    record_proc.terminate()   # arecord 종료
    record_proc.wait()
    record_proc = None

    if os.path.exists(WAV_PATH):
        full_path = os.path.abspath(WAV_PATH)
        size = os.path.getsize(WAV_PATH)
        print(f"File saved: {full_path} ({size} bytes)")
    else:
        print("No file recorded")

button.when_pressed = start_record
button.when_released = stop_record

print("Press and hold the button to record (Ctrl+C to exit)")

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Exit")

