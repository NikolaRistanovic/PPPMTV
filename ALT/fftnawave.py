import pyaudio
import wave
import matplotlib.pyplot as plt
import numpy
 
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 48000
CHUNK = 1024
RECORD_SECONDS = 2
WAVE_OUTPUT_FILENAME = "Prijem.wav"
 
audio = pyaudio.PyAudio()
 
#start
#stream = audio.open(format=FORMAT, channels=CHANNELS,
#                rate=RATE, input=True,
#                frames_per_buffer=CHUNK)
#frames = []
# 
#for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#    data = stream.read(CHUNK)
#    frames.append(data)
#
#print ("fin")

#stop
#stream.stop_stream()
#stream.close()
#audio.terminate()
 
#waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
#waveFile.setnchannels(CHANNELS)
#waveFile.setsampwidth(audio.get_sample_size(FORMAT))
#waveFile.setframerate(RATE)
#waveFile.writeframes(b''.join(frames))
#waveFile.close()

#plottin
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'r')

raw = waveFile.readframes(-1)
raw = numpy.frombuffer(raw,numpy.int16)
#time = numpy.linspace(0, len(raw)/RATE, num=len(raw))
print(len(raw))

tstep = 1/RATE
N = int(RATE * RECORD_SECONDS)

t = numpy.linspace(0, (N-1)*tstep, N)
fstep = RATE/N
f = numpy.linspace(0,(N-1)*fstep, N)

X = numpy.fft.fft(raw)
X_mag = numpy.abs(X) / N

f_plot = f[0:int(N/2+1)]
X_mag_plot = 2 * X_mag[0:int(N/2+1)]
X_mag_plot[0] = X_mag_plot[0] / 2

#X_mag_plot_diff = numpy.diff(X_mag_plot)

plt.plot(f_plot[0:47104], X_mag_plot)
#plt.plot(f_plot, X_mag_plot)
plt.show()