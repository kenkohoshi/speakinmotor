import serial
import time
import numpy as np

# データ読み込み
data = np.loadtxt("motor_freq.txt", dtype=int)

ser = serial.Serial("COM3", 115200)
time.sleep(2)

for v in data:

    # -----------------------------
    # 安定化処理（ここが重要）
    # -----------------------------

    # 低すぎる値をカット
    if v < 50:
        v = 0
    else:
        v = int(v * 2) + 80  # スケーリング

    # 上限制限
    if v > 800:
        v = 800

    ser.write(f"{v}\n".encode())
    ser.flush()

    time.sleep(0.01)

ser.close()