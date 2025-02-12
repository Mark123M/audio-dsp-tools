import matplotlib.pyplot as plt
import numpy as np

import scipy.fft

import soundfile as sf
import sounddevice as sd

def Q1():
    fn='a3/Trumpet'
    y, fs = sf.read(fn+'.wav') 

    N=len(y) 
    T=N/fs # time in seconds
    t=np.arange(N)/N*T # time samples
    f=np.arange(N)/N*fs # frequency samples
    Y=scipy.fft.fft(y)
    Yr=scipy.fft.rfft(y)
    Nr = len(Yr)

    f0 = 229
    harmonic_freq = f0 * 5  # 5th harmonic frequency

    H = np.ones_like(y)
    k = int((1100 * N) / fs)
    k2 = int((1200 * N) / fs)
    print(k, k2)

    for i in range(k, k2):
        H[i] = 0
        H[-i] = 0
    Y = Y * H

    print(N)
    print(Nr)
    y = np.real(scipy.fft.ifft(Y))
    sf.write('a3/Trump1.wav',y,fs)
    sd.play(y,fs)

    # plot
    fig, (ax0) = plt.subplots(1, 1, sharex=True)
    ax0.plot(t,y)
    ax0.set_title('Time domain')
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

    fr=np.arange(Nr)/N*fs 
    ax1.plot(f,np.abs(Y))
    ax1.set_title('FFT (abs)')

    ax2.plot(fr,np.abs(Yr))
    ax2.set_title('RFFT (abs)')

    #ax_win.plot(th,h)
    #ax_win.set_title('Filter impulse response: ' + fh)
    #ax_win.margins(0, 0.1)
    plt.savefig('fft.png')

    fig.tight_layout()

    fig.show()

    plt.show()

def Q2():
    fn='a3/Trumpet'
    y, fs = sf.read(fn+'.wav') 

    N=len(y) 
    T=N/fs # time in seconds
    t=np.arange(N)/N*T # time samples
    f=np.arange(N)/N*fs # frequency samples
    Y=scipy.fft.fft(y)
    Yr=scipy.fft.rfft(y)
    Nr = len(Yr)

    f0 = 229
    harmonic_freq = f0 * 5  # 5th harmonic frequency

    H = np.ones_like(y)
    k = int((1140 * N) / fs)
    k2 = int((1170 * N) / fs)
    print(k, k2)

    for i in range(k, k2):
        H[i] = 10 ** 0.5
        H[-i] = 10 ** 0.5
    Y = Y * H

    print(N)
    print(Nr)
    y = np.real(scipy.fft.ifft(Y))
    sf.write('a3/Trump2.wav',y,fs)
    sd.play(y,fs)

    # plot
    fig, (ax0) = plt.subplots(1, 1, sharex=True)
    ax0.plot(t,y)
    ax0.set_title('Time domain')
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

    fr=np.arange(Nr)/N*fs 
    ax1.plot(f,np.abs(Y))
    ax1.set_title('FFT (abs)')

    ax2.plot(fr,np.abs(Yr))
    ax2.set_title('RFFT (abs)')

    #ax_win.plot(th,h)
    #ax_win.set_title('Filter impulse response: ' + fh)
    #ax_win.margins(0, 0.1)
    plt.savefig('fft.png')

    fig.tight_layout()

    fig.show()

    plt.show()

def Q3():
    fn='a3/Oboe'
    y, fs = sf.read(fn+'.wav') 

    N=len(y) 
    T=N/fs # time in seconds
    t=np.arange(N)/N*T # time samples
    f=np.arange(N)/N*fs # frequency samples
    Y=scipy.fft.fft(y)
    Yr=scipy.fft.rfft(y)
    Nr = len(Yr)

    f0 = 229
    harmonic_freq = f0 * 5  # 5th harmonic frequency

    H = np.ones_like(y)
    k = int((680 * N) / fs)
    k2 = int((725 * N) / fs)
    print(k, k2)

    for i in range(k, k2):
        H[i] = 0
        H[-i] = 0
    Y = Y * H

    print(N)
    print(Nr)
    y = np.real(scipy.fft.ifft(Y))
    sf.write('a3/Oboe1.wav',y,fs)
    sd.play(y,fs)

    # plot
    fig, (ax0) = plt.subplots(1, 1, sharex=True)
    ax0.plot(t,y)
    ax0.set_title('Time domain')
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

    fr=np.arange(Nr)/N*fs 
    ax1.plot(f,np.abs(Y))
    ax1.set_title('FFT (abs)')

    ax2.plot(fr,np.abs(Yr))
    ax2.set_title('RFFT (abs)')

    #ax_win.plot(th,h)
    #ax_win.set_title('Filter impulse response: ' + fh)
    #ax_win.margins(0, 0.1)
    plt.savefig('fft.png')

    fig.tight_layout()

    fig.show()

    plt.show()

def Q4():
    fn='a3/Oboe'
    y, fs = sf.read(fn+'.wav') 

    N=len(y) 
    T=N/fs # time in seconds
    t=np.arange(N)/N*T # time samples
    f=np.arange(N)/N*fs # frequency samples
    Y=scipy.fft.fft(y)
    Yr=scipy.fft.rfft(y)
    Nr = len(Yr)

    f0 = 229
    harmonic_freq = f0 * 5  # 5th harmonic frequency

    H = np.ones_like(y)
    k = int((680 * N) / fs)
    k2 = int((720 * N) / fs)
    print(k, k2)

    for i in range(k, k2):
        H[i] = 10 ** 0.5
        H[-i] = 10 ** 0.5
    Y = Y * H

    print(N)
    print(Nr)
    y = np.real(scipy.fft.ifft(Y))
    sf.write('a3/Oboe2.wav',y,fs)
    sd.play(y,fs)

    # plot
    fig, (ax0) = plt.subplots(1, 1, sharex=True)
    ax0.plot(t,y)
    ax0.set_title('Time domain')
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

    fr=np.arange(Nr)/N*fs 
    ax1.plot(f,np.abs(Y))
    ax1.set_title('FFT (abs)')

    ax2.plot(fr,np.abs(Yr))
    ax2.set_title('RFFT (abs)')

    #ax_win.plot(th,h)
    #ax_win.set_title('Filter impulse response: ' + fh)
    #ax_win.margins(0, 0.1)
    plt.savefig('fft.png')

    fig.tight_layout()

    fig.show()

    plt.show()
#Q1()
#Q2()
Q3()
#Q4()