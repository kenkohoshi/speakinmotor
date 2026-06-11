import wave

#wav = wave.open("samplefile/c9cddeac.wav", "rb")
wav = wave.open("PC_app/samplefile/c9cddeac.wav", "rb")
fs = wav.getframerate()

print("サンプリング周波数:", fs, "Hz")
print("サンプリング周期:", 1/fs, "秒")