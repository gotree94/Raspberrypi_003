import serial
import time
from gpiozero import LED

ble_serial = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1.0)

led1 = LED(4)
led2 = LED(17)

try:
    while True:
        if ble_serial.in_waiting > 0:
            recv_data = ble_serial.readline().decode().strip()
            print(recv_data)

            if "LED1 ON" in recv_data.upper():
                led1.on()
                print("LED ON")
            elif "LED1 OFF" in recv_data.upper():
                led1.off()
                print("LED OFF")
            elif "LED2 ON" in recv_data.upper():
                led2.on()
                print("LED OFF")
            elif "LED2 OFF" in recv_data.upper():
                led2.off()
                print("LED OFF")

except KeyboardInterrupt:
    ble_serial.close()
    led1.off()
    led2.off()
    print("end")



