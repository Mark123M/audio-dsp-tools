import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf
import sounddevice as sd
fs=44100
T=2
N=T*fs
t=np.arange(N)/fs
f=220
#f=329.63
#f=400

y = 1000 * np.cos(2*np.pi*f*t)
#y = 0.177827941 * (1 - 4 * np.abs(1/2 - np.modf(f * t + 1/4)[0]))
#y = 0.25 * (4 * np.floor(f * t) - 2 * np.floor(2 * f * t) + 1)
#y = sf.read('a1/tone.wav')[0] + sf.read('a1/tri.wav')[0] + sf.read('a1/sqr.wav')[0]
y = np.sign(y) * np.minimum(np.abs(y), np.ones(N)) # Clipping

sf.write('a1/clipped.wav',y,fs)
sd.play(y,fs)

plt.plot(t,y)
plt.xlabel('time (seconds)')
plt.ylabel('value')
plt.title('A3tone')
plt.show()
