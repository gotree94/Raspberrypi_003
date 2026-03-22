from gpiozero import Button
import time

SW1 = Button(5, pull_up=False)

old_value = 0
new_value = 0

try:
    while True:
        new_value = SW1.is_pressed
        if new_value != old_value:
            old_value = new_value
            
            if new_value == 1:
                print("click")
            
            time.sleep(0.2)

except KeyboardInterrupt:
    print("end")

