"""
TCP/IP LED 클라이언트 - PC에서 실행
실행: python3 tcp_client.py
"""

import socket

SERVER_IP = "192.168.0.100"   # 라즈베리파이 IP로 변경
PORT = 9999

def send_command(cmd):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_IP, PORT))
        s.sendall(cmd.encode())
        response = s.recv(1024).decode()
        print(f"[응답] {response.strip()}")

print("명령어: ON / OFF / quit")
while True:
    cmd = input("입력> ").strip().upper()
    if cmd == "QUIT":
        break
    if cmd in ("ON", "OFF"):
        send_command(cmd)
    else:
        print("ON 또는 OFF만 입력하세요")
