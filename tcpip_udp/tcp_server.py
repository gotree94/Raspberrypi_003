"""
TCP/IP LED 서버 - 라즈베리파이 4
GPIO 17번에 LED 연결
실행: python3 tcp_server.py
"""

import socket
import RPi.GPIO as GPIO

LED_PIN = 17
HOST = "0.0.0.0"
PORT = 9999

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(1)
print(f"[TCP] 서버 대기 중... {HOST}:{PORT}")

try:
    while True:
        conn, addr = server.accept()
        print(f"[TCP] 접속: {addr}")
        data = conn.recv(1024).decode().strip().upper()
        if data == "ON":
            GPIO.output(LED_PIN, GPIO.HIGH)
            conn.sendall(b"LED ON\n")
            print("[TCP] LED ON")
        elif data == "OFF":
            GPIO.output(LED_PIN, GPIO.LOW)
            conn.sendall(b"LED OFF\n")
            print("[TCP] LED OFF")
        else:
            conn.sendall(b"ERROR: ON or OFF\n")
        conn.close()
except KeyboardInterrupt:
    print("\n종료")
finally:
    server.close()
    GPIO.cleanup()
