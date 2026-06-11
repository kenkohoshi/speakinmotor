from scipy.io import wavfile
from scipy.signal import spectrogram
import matplotlib.pyplot as plt
import numpy as np

# WAV読み込み
fs, data = wavfile.read(
    r"C:\Users\Owner\Desktop\speakingmotor\PC_app\samplefile\c9cddeac.wav"
)

print("サンプリング周波数:", fs, "Hz")
print("元のshape:", data.shape)

# ステレオならモノラル化
if len(data.shape) == 2:
    data = data.mean(axis=1)

print("変換後shape:", data.shape)

# スペクトログラム計算
f, t, Sxx = spectrogram(
    data,
    fs=fs,
    nperseg=1024,
    noverlap=512
)

# dB表示
Sxx_db = 10 * np.log10(Sxx + 1e-10)

# 描画
plt.figure(figsize=(10, 5))
plt.pcolormesh(t, f, Sxx_db, shading="gouraud")
plt.ylabel("Frequency [Hz]")
plt.xlabel("Time [sec]")
plt.title("Spectrogram")
plt.colorbar(label="Power [dB]")
plt.ylim(0, 5000)  # 人の声が見やすい範囲
plt.show()