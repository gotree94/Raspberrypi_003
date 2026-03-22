from gpiozero import Button
import time

button = Button(5, pull_up=False, bounce_time=0.02)

def on_press():
    print("Button pressed")
    print("Recording...")

def on_release():
    print("Button released")
    print("Stop recording")

button.when_pressed = on_press
button.when_released = on_release

print("Button condition test started (Ctrl+C to exit)")

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Exit")

