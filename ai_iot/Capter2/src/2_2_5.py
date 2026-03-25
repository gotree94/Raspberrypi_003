from gpiozero import Button

SW1 = Button(5, pull_up=False)
SW2 = Button(6, pull_up=False)
SW3 = Button(13, pull_up=False)
SW4 = Button(19, pull_up=False)

def handle_sw1():
    print("SW1 pressed")

def handle_sw2():
    print("SW2 pressed")

def handle_sw3():
    print("SW3 pressed")

def handle_sw4():
    print("SW4 pressed")

SW1.when_pressed = handle_sw1
SW2.when_pressed = handle_sw2
SW3.when_pressed = handle_sw3
SW4.when_pressed = handle_sw4

try:
    while True :
        pass

except KeyboardInterrupt:
    print("end")
