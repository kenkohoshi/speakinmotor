import serial
import time
import numpy as np

data = np.loadtxt("motor_freq.txt", dtype=int)

ser = serial.Serial("COM3", 115200)
time.sleep(2)

for v in data:
    ser.write(f"{v}\n".encode())
    time.sleep(0.01)

ser.close()