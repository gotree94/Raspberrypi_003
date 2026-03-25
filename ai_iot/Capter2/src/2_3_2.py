from gpiozero import PWMLED
import time

led_R = PWMLED(10)
led_G = PWMLED(9)
led_B = PWMLED(11)

try:
    while True:
        led_R.value = 0.0
        led_G.value = 0.0
        led_B.value = 0.0
        time.sleep(1.0)
        
        led_R.value = 0.5
        led_G.value = 0.5
        led_B.value = 0.5
        time.sleep(1.0)
        
        led_R.value = 1.0
        led_G.value = 1.0
        led_B.value = 1.0
        time.sleep(1.0)

except KeyboardInterrupt:
    led_R.off()
    led_G.off()
    led_B.off()
    print("end")

