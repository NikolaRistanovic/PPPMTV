import numpy as np
import matplotlib.pyplot as plt

Fs = 48000
tstep = 1 / Fs
f0 = 1000

N = int(Fs / f0)

t = np.linspace(0, (N-1)*tstep, N)
fstep = Fs/N
f = np.linspace(0,(N-1)*fstep, N)

y = 1 * np.sin(2 * np.pi * f0 * t)

X = np.fft.fft(y)
X_mag = np.abs(X) / N

f_plot = f[0:int(N/2+1)]
X_mag_plot = 2 * X_mag[0:int(N/2+1)]
X_mag_plot[0] = X_mag_plot[0] / 2

plt.plot(f_plot, X_mag_plot)
plt.show()

