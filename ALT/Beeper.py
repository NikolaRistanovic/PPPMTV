import time
import pyaudio
import numpy as np

p = pyaudio.PyAudio()

FORMAT = pyaudio.paFloat32
CHANNELS = 1
RATE = 48000
DURATION = 0.25

print("Ukucajte broj tonova, pa zatim frekvencije jedno po jedno:")
FREQUENCIES = []
NUM_TONES = input()
NUM_TONES = int(NUM_TONES)

for i in range(NUM_TONES):
    FREQUENCIES.append(int(input()))

for i in range(NUM_TONES):
    print("playing frequency ",i,"which is ",FREQUENCIES[i])
    samples = (np.sin(2 * np.pi * np.arange(RATE * DURATION) * FREQUENCIES[i] / RATE)).astype(np.float32).tobytes()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    output=True)

    stream.write(samples)

    stream.stop_stream()
    stream.close()

p.terminate()
