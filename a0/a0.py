import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf
import sounddevice as sd
fs=44100
T=4
N=T*fs
t=np.arange(N)/fs
#f=220
f1 = 329.63
f2 = 659.26
y1 = 0.25 * np.cos(2*np.pi*f1*t)
y2 = 0.25 * np.cos(2*np.pi*f2*t)
#sf.write('a0/A3tone'+'.wav',y,fs)
#sf.write('a0/E4tone'+'.wav',y,fs)
y1 = sf.read('a0/A3note.wav')[0]
y2 = sf.read('a0/E4note.wav')[0]
y = y1 + y2
sf.write('a0/A3E4note.wav',y,fs)

sd.play(y,fs)
plt.plot(t,y)
plt.xlabel('time (seconds)')
plt.ylabel('value')
plt.title('A3tone')
plt.show()
