import socket
import time

ESP32_IP = "192.168.1.128"
PORT = 5000

with open(r"C:\\Users\\Owner\\Desktop\\speakingmotor\\motor_freq.csv", "r") as f:
    lines = f.readlines()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ESP32_IP, PORT))

for line in lines:
    line = line.strip()

    if not line:
        continue

    sock.send((line + '\n').encode())  # ←改行を保証

    time.sleep(0.005)  # ←少し遅くする（重要）

sock.close()