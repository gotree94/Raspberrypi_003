from gpiozero import PWMLED
import time

led_R = PWMLED(10)
led_G = PWMLED(9)
led_B = PWMLED(11)

colors = [
    (1.0, 0.0, 0.0),  
    (1.0, 0.5, 0.0),  
    (1.0, 1.0, 0.0),  
    (0.0, 1.0, 0.0), 
    (0.0, 0.0, 1.0), 
    (0.3, 0.0, 0.5),  
    (0.6, 0.0, 1.0), 
]

try:
    while True:
        for r, g, b in colors:
            led_R.value = r
            led_G.value = g
            led_B.value = b
            time.sleep(1.0)

except KeyboardInterrupt:
    led_R.off()
    led_G.off()
    led_B.off()
    print("end")
