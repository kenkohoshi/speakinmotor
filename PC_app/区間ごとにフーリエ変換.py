from scipy.io import wavfile
from scipy.signal import spectrogram
import numpy as np

# WAV読み込み
fs, data = wavfile.read(
    r"C:\Users\Owner\Desktop\speakingmotor\PC_app\samplefile\c9cddeac.wav"
)

print("サンプリング周波数:", fs, "Hz")
print("元のshape:", data.shape)

# ステレオ→モノラル
if len(data.shape) == 2:
    data = data.mean(axis=1)

print("変換後shape:", data.shape)

# STFT
f, t, Sxx = spectrogram(
    data,
    fs=fs,
    nperseg=1024,
    noverlap=512
)

print("周波数ビン数:", len(f))
print("時間ステップ数:", len(t))
print("Sxx shape:", Sxx.shape)

# 4帯域に分割
band1 = Sxx[(f >= 100) & (f < 300)].sum(axis=0)
band2 = Sxx[(f >= 300) & (f < 600)].sum(axis=0)
band3 = Sxx[(f >= 600) & (f < 1200)].sum(axis=0)
band4 = Sxx[(f >= 1200) & (f < 3000)].sum(axis=0)

# 0～255へ正規化
motor1 = (band1 / np.max(band1) * 255).astype(int)
motor2 = (band2 / np.max(band2) * 255).astype(int)
motor3 = (band3 / np.max(band3) * 255).astype(int)
motor4 = (band4 / np.max(band4) * 255).astype(int)

print("\nMotor1:")
print(motor1[100:120])

print("\nMotor2:")
print(motor2[100:120])

print("\nMotor3:")
print(motor3[100:120])

print("\nMotor4:")
print(motor4[100:120])

# CSV保存
output = np.column_stack((t, motor1, motor2, motor3, motor4))

np.savetxt(
    "motor_data.csv",
    output,
    delimiter=",",
    header="time,motor1,motor2,motor3,motor4",
    comments="",
    fmt=["%.4f", "%d", "%d", "%d", "%d"]
)

print("Motor1 max =", np.max(motor1))
print("Motor2 max =", np.max(motor2))
print("Motor3 max =", np.max(motor3))
print("Motor4 max =", np.max(motor4))

print("\nmotor_data.csv を保存しました")