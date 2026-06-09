import numpy as np
from scipy.io import wavfile

fs, data = wavfile.read("samplefile/input.wav")

# モノラル化
if len(data.shape) > 1:
    data = data[:, 0]

window_size = 1024
step_data = []

for i in range(0, len(data) - window_size, window_size):
    chunk = data[i:i+window_size]

    # FFT
    spectrum = np.fft.fft(chunk)
    freqs = np.fft.fftfreq(len(chunk), 1/fs)

    # 正の周波数だけ
    idx = np.argmax(np.abs(spectrum[:len(spectrum)//2]))
    freq = abs(freqs[idx])

    # モータ用に変換（スケーリング）
    motor_speed = int(freq)

    step_data.append(motor_speed)

# 保存
np.savetxt("motor_freq.txt", step_data, fmt="%d")