import pyaudio
import scipy.io.wavfile
import wave
import matplotlib.pyplot as plt
import numpy
 
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 48000
CHUNK = 1024
RECORD_SECONDS = 3
WAVE_OUTPUT_FILENAME = "Prijem.wav"
 
audio = pyaudio.PyAudio()
 
#start
stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=RATE)
frames = []
 
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print ("fin")

#stop
stream.stop_stream()
stream.close()
audio.terminate()
data = numpy.frombuffer(data,numpy.int16)

file_to_save = scipy.io.wavfile.write(WAVE_OUTPUT_FILENAME, RATE, data*CHUNK)

#plottin
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'r')
raw = waveFile.readframes(-1)
raw = numpy.frombuffer(raw,numpy.int16)
time = numpy.linspace(0, len(raw)/RATE, num=len(raw))

print(len(raw))
plt.plot(time, raw)
plt.show()
