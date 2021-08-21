import pyaudio
import scipy.io.wavfile
import numpy as np
import matplotlib.pyplot as plt
import wave

p = pyaudio.PyAudio()

FORMAT = pyaudio.paFloat32
RATE = 44100
DURATION = 1
FREQ = 1000
CHANNELS = 1
FILENAME = "TestSine.wav"

samples = (np.sin(2 * np.pi * np.arange(RATE * DURATION) * FREQ / RATE))
samples = (samples * 32767).astype(np.int16)
file_to_save = scipy.io.wavfile.write(FILENAME, RATE, samples)

waveFile = wave.open(FILENAME, 'r')

raw = waveFile.readframes(-1)
raw = np.frombuffer(raw,np.int16)
time = np.linspace(0, len(raw)/RATE, num=len(raw))
print(len(raw))
plt.plot(time, raw)
plt.show()