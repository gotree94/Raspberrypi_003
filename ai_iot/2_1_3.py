from gpiozero import LED
import time

led1 = LED(4)
led2 = LED(17)
led3 = LED(27)
led4 = LED(22)

try :
    while True :
        led1.on()
        led2.on()
        led3.on()
        led4.on()
        time.sleep(1.0)
        led1.off()
        led2.off()
        led3.off()
        led4.off()
        time.sleep(1.0)

except KeyboardInterrupt:
    led1.off()
    led2.off()
    led3.off()
    led4.off()
    print("end")
