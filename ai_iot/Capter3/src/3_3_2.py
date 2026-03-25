import serial
from gpiozero import Button

ble_serial = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1.0)

SW1 = Button(5, pull_up=False)
SW2 = Button(6, pull_up=False)

def handle_sw1():
    print("SW1 pressed")
    ble_serial.write( "SW1 pressed\r\n".encode() )

def handle_sw2():
    print("SW2 pressed")
    ble_serial.write( "SW2 pressed\r\n".encode() )

SW1.when_pressed = handle_sw1
SW2.when_pressed = handle_sw2

try:
    while True :
        pass

except KeyboardInterrupt:
    print("end")


