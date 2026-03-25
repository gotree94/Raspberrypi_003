import serial
import time

ble_serial = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1.0)

try:
    while True :
        send_data = "I am raspberry pi \r\n"
        ble_serial.write( send_data.encode() )
        time.sleep(1.0)
        
except KeyboardInterrupt:
    ble_serial.close()
    print("end")