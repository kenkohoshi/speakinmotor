import socket
import time

ESP32_IP = "192.168.1.128"
PORT = 5000

# ファイル読み込み

#with open("motor_freq.txt", "r") as f:
with open(r"C:\\Users\\Owner\\Desktop\\speakingmotor\\PC_app\\motor_freq.txt", "r") as f:
    lines = f.readlines()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ESP32_IP, PORT))

for line in lines:
    sock.send(line.encode())  # 1行ずつ送る
    time.sleep(0.001)         # 遅延（重要）

sock.close()