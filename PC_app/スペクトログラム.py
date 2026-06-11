from scipy.io import wavfile
from scipy.signal import spectrogram
import matplotlib.pyplot as plt
import numpy as np

fs, data = wavfile.read("PC_app/samplefile/c9cddeac.wav")

print("fs =", fs)
print("shape =", data.shape)

# ステレオ→左チャンネルだけ使う
if len(data.shape) == 2:
    data = data[:, 0]

print("after shape =", data.shape)

f, t, Sxx = spectrogram(data, fs)

plt.pcolormesh(t, f, 10*np.log10(Sxx + 1e-10))
plt.ylabel("Frequency [Hz]")
plt.xlabel("Time [sec]")
plt.colorbar(label="Power (dB)")
plt.show()