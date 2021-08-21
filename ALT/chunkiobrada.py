import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import wave

p = pyaudio.PyAudio()

FORMAT = pyaudio.paFloat32
CHANNELS = 1
RATE = 48000
RECORD_SECONDS = 2
WAVE_OUTPUT_FILENAME = "prijem.wav"

waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'r')
raw = waveFile.readframes(-1)
raw = np.frombuffer(raw,np.int16)

BitLength = 480
Bit_time = np.linspace(0, (BitLength-1), num = BitLength)

tstep = 1/RATE
N = int(RATE * RECORD_SECONDS)

t = np.linspace(0, (N-1)*tstep, N)
fstep = RATE/N
buffer = np.arange(0,48000)
for i in range(48000):
    buffer[i] = 0

for i in range(0,int(len(raw)/BitLength)):
    Bit_chunked = raw[i * BitLength:((i * BitLength) + BitLength)]

    buffer[0:BitLength] = Bit_chunked

    X = np.fft.fft(buffer)
    X_mag = np.abs(X) / N

    f = np.arange(0,24000)
    f_plot = f[0:24000]
    X_mag_plot = 2 * X_mag[0:int(N/2+1)]
    X_mag_plot[0] = X_mag_plot[0] / 2

    print(len(X_mag_plot)//2)

    plt.plot(f_plot, X_mag_plot[0:len(X_mag_plot)//2])
    plt.show()