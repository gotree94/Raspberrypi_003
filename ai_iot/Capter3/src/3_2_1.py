import serial
import time
from gpiozero import LED

ble_serial = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1.0)

try:
    while True:
        if ble_serial.in_waiting > 0:
            recv_data = ble_serial.readline().decode().strip()
            print(recv_data)

            if recv_data.upper() == "LED ON":
                print("LED ON")
            elif recv_data.upper() == "LED OFF":
                print("LED OFF")

except KeyboardInterrupt:
    ble_serial.close()
    print("end")
