import socket
import time
import csv

ESP32_IP = "192.168.1.128"
PORT = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ESP32_IP, PORT))

with open(
    r"C:\Users\Owner\Desktop\speakingmotor\PC_app\motor_data.csv",
    "r",
    newline=""
) as f:

    reader = csv.reader(f)

    next(reader)  # ヘッダ行を飛ばす

    for row in reader:

        motor1 = row[1]  # 左から2列目

        sock.send((motor1 + "\n").encode())

        time.sleep(0.0116)

sock.close()