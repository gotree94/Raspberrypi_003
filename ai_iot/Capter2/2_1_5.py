from gpiozero import OutputDevice
import time

led1 = OutputDevice(4)

try:
    while True:
        led1.on()
        time.sleep(1.0)
        led1.off()
        time.sleep(1.0)

except KeyboardInterrupt:
    led1.off()
    print("end")