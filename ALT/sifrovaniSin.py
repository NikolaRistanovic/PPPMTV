import pyaudio
import numpy as np
import matplotlib.pyplot as plt
# set up binary list
binIn = [0,0,0,0,0,0,0,0]
x = bin(int(input("Ubacite int :")))
print(x)
xstring = str(x)
strlength = len(xstring)
j = 7
for i in range(strlength-1,1,-1):
    binIn[j] = int(xstring[i])
    j = j-1

if(j>0):
    for j in range(j,0,-1):
        binIn[j] = 0

print(binIn)

p = pyaudio.PyAudio()

FORMAT = pyaudio.paFloat32
CHANNELS = 1
RATE = 48000
DURATION = 0.01

FREQ_HIGH = 3000
FREQ_LOW = 1000

High_wave = (np.sin(2 * np.pi * np.arange(RATE * DURATION) * FREQ_HIGH / RATE))
Low_wave = (np.sin(2 * np.pi * np.arange(RATE * DURATION) * FREQ_LOW / RATE))
time = np.linspace(0, len(High_wave)/RATE, num=len(High_wave))

plt.plot(time, High_wave)
plt.show()

Combined_wave = np.array([])

for i in range(8):
    if(binIn[i] == 1):
        Combined_wave = np.append(Combined_wave, High_wave)
    else:
        Combined_wave = np.append(Combined_wave, Low_wave)

plt.plot(time, Combined_wave)
plt.show()