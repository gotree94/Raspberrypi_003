"""
UDP LED 클라이언트 - PC에서 실행
실행: python3 udp_client.py
"""

import socket

SERVER_IP = "192.168.0.100"   # 라즈베리파이 IP로 변경
PORT = 9998

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.settimeout(3)

print("명령어: ON / OFF / quit")
while True:
    cmd = input("입력> ").strip().upper()
    if cmd == "QUIT":
        break
    if cmd in ("ON", "OFF"):
        client.sendto(cmd.encode(), (SERVER_IP, PORT))
        try:
            response, _ = client.recvfrom(1024)
            print(f"[응답] {response.decode()}")
        except socket.timeout:
            print("[오류] 응답 없음 (타임아웃)")
    else:
        print("ON 또는 OFF만 입력하세요")

client.close()
