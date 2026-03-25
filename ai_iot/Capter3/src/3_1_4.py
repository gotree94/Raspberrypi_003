import serial
import time

ble_serial = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1.0)

try:
    while True :
        if ble_serial.in_waiting > 0:
            recv_data = ble_serial.readline().decode().strip()
            print(recv_data)
        
except KeyboardInterrupt:
    ble_serial.close()
    print("end")