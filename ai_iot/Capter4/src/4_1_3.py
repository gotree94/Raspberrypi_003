import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from gpiozero import DistanceSensor
import time

def send_email():
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    email_address = "munjjac@gmail.com"
    password = "tnil bpzr ikie vnbp"
    recipient_email = "munjjac@hanmail.net"

    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = recipient_email
    msg['Subject'] = "Package Arrival"
    message = "The ultrasonic sensor detected a package within 10 cm."
    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(email_address, password)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print("Failed to send email:", e)

sensor = DistanceSensor(echo=24, trigger=23)

try:
    while True:
        distance_cm = sensor.distance * 100
        print("cm:", distance_cm)

        if distance_cm <= 10:
            print("The package has arrived.")
            send_email()
            for _ in range(60 * 60 * 6):
                time.sleep(1.0)

        time.sleep(0.5)

except KeyboardInterrupt:
    print("Program terminated.")
