from gpiozero import Button

SW1 = Button(5, pull_up=False)

def on_click():
    print("click")

SW1.when_pressed = on_click

try:
    while True :
        pass

except KeyboardInterrupt:
    print("end")