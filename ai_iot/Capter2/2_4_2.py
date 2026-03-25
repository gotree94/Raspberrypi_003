from gpiozero import PWMOutputDevice
from time import sleep

buzzer = PWMOutputDevice(18)

notes = {
    "C": 261,
    "D": 293,
    "E": 329,
    "F": 349,
    "G": 392,
    "A": 440,
    "B": 493,
    "C5": 523,
    " ": 0
}

melody = [
    "C", "C", "G", "G", "A", "A", "G", " ",
    "F", "F", "E", "E", "D", "D", "C", " ",
    "G", "G", "F", "F", "E", "E", "D", " ",
    "G", "G", "F", "F", "E", "E", "D", " ",
    "C", "C", "G", "G", "A", "A", "G", " ",
    "F", "F", "E", "E", "D", "D", "C"
]

try:
    for note in melody:
        freq = notes[note]
        if freq == 0:
            buzzer.value = 0
        else:
            buzzer.frequency = freq
            buzzer.value = 0.5
        sleep(0.4)
        buzzer.value = 0
        sleep(0.05)

except KeyboardInterrupt:
    buzzer.off()
    print("end")
