import numpy as np
import wave

# --- wav読み込み ---
wav = wave.open("samplefile/c9cddeac.wav")
sr = wav.getframerate()
n = wav.getnframes()
audio = np.frombuffer(wav.readframes(n), dtype=np.int16)

# モノラル化（ステレオ対策）
if wav.getnchannels() == 2:
    audio = audio[::2]

# --- パラメータ ---
frame_size = int(sr * 0.02)  # 20msごと
step = []

# --- 音符化 ---
for i in range(0, len(audio), frame_size):
    frame = audio[i:i+frame_size]

    if len(frame) == 0:
        break

    # RMS（音量）
    rms = np.sqrt(np.mean(frame**2))

    # スケーリング（ここ重要）
    speed = int(np.clip(rms / 100, 0, 255))

    t = i / sr

    step.append((t, speed))

# --- 保存 ---
with open("motor_freq.csv", "w") as f:
    for t, s in step:
        f.write(f"{int(t*1000)},{s}\n")

print("done")