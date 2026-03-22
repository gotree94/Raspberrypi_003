import serial
import time
from gpiozero import LED

ble_serial = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1.0)

try:
    while True:
        if ble_serial.in_waiting > 0:
            recv_data = ble_serial.readline().decode().strip()
            print(recv_data)

            if "LED ON" in recv_data.upper():
                print("LED ON")
            elif "LED OFF" in recv_data.upper():
                print("LED OFF")

except KeyboardInterrupt:
    ble_serial.close()
    print("end")

