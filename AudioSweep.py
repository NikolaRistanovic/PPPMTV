import pyaudio
import numpy as np
import matplotlib.pyplot as plt

p = pyaudio.PyAudio()

FORMAT = pyaudio.paFloat32
CHANNELS = 1
AMPLITUDE = 1 #VOLUME
RATE = 48000
START_FREQ = 10
STOP_FREQ = 100
DURATION = 2

N = RATE * DURATION
phi = 0
f = START_FREQ
delta = (2 * np.pi * f) / RATE
f_delta = (STOP_FREQ - START_FREQ) / (RATE * DURATION)

arr = []

for i in range(0,N):
    arr.append(AMPLITUDE * np.sin(phi))
    phi = phi + delta
    f = f + f_delta
    delta = (2 * np.pi * f) / RATE

plt.plot(arr)
plt.show()

npy_array = np.array(arr)

tostream = npy_array.astype(np.float32).tobytes()

stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    output=True)

stream.write(tostream)

stream.stop_stream()
stream.close()

p.terminate()