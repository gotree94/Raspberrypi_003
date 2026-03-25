import cv2
from gpiozero import PWMOutputDevice
from time import sleep

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0)
buzzer = PWMOutputDevice(18)

alert = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) > 0:
        if not alert:
            buzzer.frequency = 440
            buzzer.value = 0.5
            sleep(0.3)
            buzzer.value = 0
            alert = True
    else:
        alert = False

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Face", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

buzzer.off()
cap.release()
cv2.destroyAllWindows()
