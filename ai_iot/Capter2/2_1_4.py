from gpiozero import LED
import time

led1 = LED(4)

try :
    while True :
        led1.value = 1
        time.sleep(1.0)
        led1.value = 0
        time.sleep(1.0)

except KeyboardInterrupt:
    led1.value = 0
    print("end")
