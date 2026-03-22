from gpiozero import PWMOutputDevice
from time import sleep

buzzer = PWMOutputDevice(18)

notes = {
    "do": 261,
    "re": 293,
    "mi": 329,
    "fa": 349,
    "sol": 392,
    "la": 440,
    "si": 493,
    "do'": 523
}

try:
    for name, freq in notes.items():
        print(name)
        buzzer.frequency = freq
        buzzer.value = 0.5
        sleep(0.5)
        buzzer.value = 0
        sleep(0.05)

except KeyboardInterrupt:
    buzzer.off()
    print("end")
