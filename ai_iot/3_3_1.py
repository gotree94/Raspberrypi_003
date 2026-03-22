from gpiozero import Button

SW1 = Button(5, pull_up=False)
SW2 = Button(6, pull_up=False)

def handle_sw1():
    print("SW1 pressed")

def handle_sw2():
    print("SW2 pressed")

SW1.when_pressed = handle_sw1
SW2.when_pressed = handle_sw2

try:
    while True :
        pass

except KeyboardInterrupt:
    print("end")

