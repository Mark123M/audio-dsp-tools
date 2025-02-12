import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf
import sounddevice as sd
fs=44100
T=2
N=T*fs
t=np.arange(N)/fs
f=440
#f=329.63
#f=400

#y = 1000 * np.cos(2*np.pi*f*t)

#y = 0.177827941 * (1 - 4 * np.abs(1/2 - np.modf(f * t + 1/4)[0]))
#y = 0.25 * (4 * np.floor(f * t) - 2 * np.floor(2 * f * t) + 1)
#y = sf.read('a1/tone.wav')[0] + sf.read('a1/tri.wav')[0] + sf.read('a1/sqr.wav')[0]
y = np.zeros_like(t)

def pure_tone(i, ai, si):
    return ai * np.cos(2*np.pi*i*f*(t) + si)

def add_tones(an, sn, y):
    for i in range(1, 10):
        y += pure_tone(i, an[i - 1], sn[i - 1])

sine_shift = -np.pi / 2
saw_scale = -2 / np.pi
#add_tones([1, 0, 1/3, 0, 1/5, 0, 1/7, 0, 1/9], [sine_shift, 0, sine_shift, 0, sine_shift, 0, sine_shift, 0, sine_shift], y)
#add_tones([1, 0, -1/9, 0, 1/25, 0, -1/49, 0, 1/81], [sine_shift, 0, sine_shift, 0, sine_shift, 0, sine_shift, 0, sine_shift], y)
#add_tones([-1 * saw_scale, 1/2 * saw_scale, -1/3 * saw_scale, 1/4 * saw_scale, -1/5 * saw_scale, 1/6 * saw_scale, -1/7 * saw_scale, 1/8 * saw_scale, -1/9 * saw_scale], [sine_shift, sine_shift, sine_shift, sine_shift, sine_shift, sine_shift, sine_shift, sine_shift, sine_shift], y)
add_tones([ 0.05, 0.15, 0.22, 0.22, 0.17, 0.10, 0.05, 0.02, 0.008], [0, np.pi/2, 0, -np.pi/2, 0, np.pi/2, 0, -np.pi/2, 0], y)
y = (1/2) * y
# normalize
#min_val = np.min(y)
#max_val = np.max(y)
#y = 2 * (y - min_val) / (max_val - min_val) - 1

#y = np.sign(y) * np.minimum(np.abs(y), np.ones(N)) # Clipping


sf.write('a2/new/file4.wav',y,fs)
sd.play(y,fs)

plt.plot(t,y)
plt.xlabel('time (seconds)')
plt.ylabel('value')
plt.title('A3tone')
plt.show()
