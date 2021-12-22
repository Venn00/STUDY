import numpy as np
import matplotlib.pyplot as plt

Fs = 2000 # Sampling freq
tstep = 1 / Fs
f0 = 100

N = int(20 * Fs / f0) # number of samples

t = np.linspace(0, (N-1)*tstep, N) # time steps
fstep = Fs / N # freq interval
f = np.linspace(0, (N-1)*fstep, N) # freq steps

y = 1 * np.sin(2 * np.pi * f0 * t) + 1 * np.sin(5 * np.pi * f0 * t)

# perform fft
X = np.fft.fft(y)
X_mag = np.abs(X) / N 


f_plot = f[0:int(N/2+1)]
X_mag_plot = 2 * X_mag[0:int(N/2+1)]
X_mag_plot[0] = X_mag_plot[0] / 2


#plot
fig, [ax1, ax2] = plt.subplots(nrows = 2, ncols = 1)
ax1.plot(t, y)
ax2.plot(f_plot, X_mag_plot)
plt.show()
