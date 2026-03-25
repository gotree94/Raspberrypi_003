from gpiozero import DistanceSensor
import time

sensor = DistanceSensor(echo=24, trigger=23)

try:
    while True:
        distanceCm = sensor.distance * 100
        print('cm: ', distanceCm)
        
        if distanceCm <= 10 :
            print("The package has arrived")
            for i in range(60*60*6): #6hours
                time.sleep(1.0)
        time.sleep(0.5)

except KeyboardInterrupt:
    pass