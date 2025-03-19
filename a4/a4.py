import matplotlib.pyplot as plt
import numpy as np

import scipy.fft
import scipy.signal as signal

import soundfile as sf
import sounddevice as sd

def Q1():
    h, fs = sf.read('a4/A4-LPF_fir.wav')
    y, fs = sf.read('a4/Trumpet.wav')
    yfilt = signal.lfilter(h, 1, y)

    sf.write('a4/Trump_LP.wav',yfilt,fs)
    sd.play(yfilt,fs)

    N=len(yfilt)
    T=N/fs # time in seconds
    t=np.arange(N)/N*T # time samples
    plt.plot(t,yfilt)
    plt.xlabel('time (seconds)')
    plt.ylabel('value')
    plt.title('A3tone')
    plt.show()

def Q2():
    h, fs = sf.read('a4/A4-HPF_fir.wav')
    y, fs = sf.read('a4/Trumpet.wav')
    yfilt = signal.lfilter(h, 1, y)

    sf.write('a4/Trump_HP.wav',yfilt,fs)
    sd.play(yfilt,fs)

    N=len(yfilt)
    T=N/fs # time in seconds
    t=np.arange(N)/N*T # time samples
    plt.plot(t,yfilt)
    plt.xlabel('time (seconds)')
    plt.ylabel('value')
    plt.title('A3tone')
    plt.show()

def Q3():
    h, fs = sf.read('a4/A4-BPF_fir.wav')
    y, fs = sf.read('a4/Trumpet.wav')
    yfilt = signal.lfilter(h, 1, y)

    sf.write('a4/Trump_BP.wav',yfilt,fs)
    sd.play(yfilt,fs)

    N=len(yfilt)
    T=N/fs # time in seconds
    t=np.arange(N)/N*T # time samples
    plt.plot(t,yfilt)
    plt.xlabel('time (seconds)')
    plt.ylabel('value')
    plt.title('A3tone')
    plt.show()

def Q4():
    h1, fs = sf.read('a4/A4-LPF_fir.wav')
    h2, fs = sf.read('a4/A4-HPF_fir.wav')
    y, fs = sf.read('a4/Trumpet.wav')
    yfilt = signal.lfilter(h1, 1, y)
    yfilt = signal.lfilter(h2, 1, yfilt)

    sf.write('a4/Trump_LPHP.wav',yfilt,fs)
    sd.play(yfilt,fs)

    N=len(yfilt)
    T=N/fs # time in seconds
    t=np.arange(N)/N*T # time samples
    plt.plot(t,yfilt)
    plt.xlabel('time (seconds)')
    plt.ylabel('value')
    plt.title('A3tone')
    plt.show()

def Q5():
    h1, fs = sf.read('a4/A4-BPF_fir.wav')
    #h2, fs = sf.read('a4/A4-HPF_fir.wav')
    y, fs = sf.read('a4/Oboe.wav')
    yfilt = signal.lfilter(h1, 1, y)
    #yfilt = signal.lfilter(h2, 1, yfilt)

    sf.write('a4/Oboe_BP.wav',yfilt,fs)
    sd.play(yfilt,fs)

    N=len(yfilt)
    T=N/fs # time in seconds
    t=np.arange(N)/N*T # time samples
    plt.plot(t,yfilt)
    plt.xlabel('time (seconds)')
    plt.ylabel('value')
    plt.title('A3tone')
    plt.show()

def Q6():
    h1, fs = sf.read('a4/A4-LPF_fir.wav')
    h2, fs = sf.read('a4/A4-HPF_fir.wav')
    y, fs = sf.read('a4/Oboe.wav')
    yfilt = signal.lfilter(h1, 1, y)
    yfilt = signal.lfilter(h2, 1, yfilt)

    sf.write('a4/Oboe_LPHP.wav',yfilt,fs)
    sd.play(yfilt,fs)

    N=len(yfilt)
    T=N/fs # time in seconds
    t=np.arange(N)/N*T # time samples
    plt.plot(t,yfilt)
    plt.xlabel('time (seconds)')
    plt.ylabel('value')
    plt.title('A3tone')
    plt.show()
#Q1()
#Q2()
#Q3()
#Q4()
#Q5()
#Q6()