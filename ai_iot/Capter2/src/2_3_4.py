from gpiozero import PWMOutputDevice
import time

led_R = PWMOutputDevice(10)

try:
    while True:
        led_R.value = 0.0 
        time.sleep(1)
        led_R.value = 0.5 
        time.sleep(1)
        led_R.value = 1.0 
        time.sleep(1)

except KeyboardInterrupt:
    led_R.off()
    print("end")
