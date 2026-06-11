from scipy.io import wavfile
from scipy.signal import spectrogram
import matplotlib.pyplot as plt
import numpy as np

# WAV読み込み
fs, data = wavfile.read(
    r"C:\Users\Owner\Desktop\speakingmotor\PC_app\samplefile\c9cddeac.wav"
)

# ステレオ→モノラル
if len(data.shape) == 2:
    data = data.mean(axis=1)

# STFT
f, t, Sxx = spectrogram(
    data,
    fs=fs,
    nperseg=1024,
    noverlap=512
)

# ===== 4帯域 =====
band1 = Sxx[(f >= 100) & (f < 300)].sum(axis=0)
band2 = Sxx[(f >= 300) & (f < 600)].sum(axis=0)
band3 = Sxx[(f >= 600) & (f < 1200)].sum(axis=0)
band4 = Sxx[(f >= 1200) & (f < 3000)].sum(axis=0)

# 正規化（0～1）
band1 /= np.max(band1)
band2 /= np.max(band2)
band3 /= np.max(band3)
band4 /= np.max(band4)

# グラフ
plt.figure(figsize=(12,6))

plt.plot(t, band1, label="100-300Hz")
plt.plot(t, band2, label="300-600Hz")
plt.plot(t, band3, label="600-1200Hz")
plt.plot(t, band4, label="1200-3000Hz")

plt.xlabel("Time [s]")
plt.ylabel("Normalized Power")
plt.title("4 Frequency Bands")
plt.legend()
plt.grid()

plt.show()