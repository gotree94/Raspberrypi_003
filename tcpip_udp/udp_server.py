"""
UDP LED 서버 - 라즈베리파이 4
GPIO 17번에 LED 연결
실행: python3 udp_server.py
"""

import socket
import RPi.GPIO as GPIO

LED_PIN = 17
HOST = "0.0.0.0"
PORT = 9998

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))
print(f"[UDP] 서버 대기 중... {HOST}:{PORT}")

try:
    while True:
        data, addr = server.recvfrom(1024)
        cmd = data.decode().strip().upper()
        print(f"[UDP] {addr} → {cmd}")
        if cmd == "ON":
            GPIO.output(LED_PIN, GPIO.HIGH)
            server.sendto(b"LED ON", addr)
            print("[UDP] LED ON")
        elif cmd == "OFF":
            GPIO.output(LED_PIN, GPIO.LOW)
            server.sendto(b"LED OFF", addr)
            print("[UDP] LED OFF")
        else:
            server.sendto(b"ERROR: ON or OFF", addr)
except KeyboardInterrupt:
    print("\n종료")
finally:
    server.close()
    GPIO.cleanup()
