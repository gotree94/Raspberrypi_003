from gpiozero import PWMLED
import time

led = PWMLED(10)  

try:
    while True:
        led.value = 0.0
        time.sleep(1.0)
        
        led.value = 0.3
        time.sleep(1.0)
        
        led.value = 0.6
        time.sleep(1.0)
        
        led.value = 1.0
        time.sleep(1.0)

except KeyboardInterrupt:
    led.off()
    print("end")
