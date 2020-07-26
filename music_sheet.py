import numpy as np 
import random
from matplotlib import pyplot as plt
from scipy.io import wavfile


def info_popup():
    print("Enter the Music Letter Notes accordingly")
    print("Enter * for no music area")
def concate_array(final_array,sine_array):
    for i in range(len(sine_array)):
        final_array.append(sine_array[i])
table=np.array([[ord('1'),65.41],   #   c2
               [ord('2'),73.42],    #   d2
               [ord('3'),82.41],    #   e2
               [ord('4'),87.31],    #   f2
               [ord('5'),98],       #   g2
               [ord('6'),110],      #   a2
               [ord('7'),123.47],   #   b2
               [ord('8'),130.81],   #   c3
               [ord('9'),146.83],   #   d3
               [ord('0'),164.81],   #   e3
               [ord('q'),174.61],   #   f3
               [ord('w'),196],      #   g3
               [ord('e'),220],      #   a3
               [ord('r'),246.94],   #   b3
               [ord('t'),261.63],   #   c4
               [ord('y'),293.66],   #   d4
               [ord('u'),359.63],   #   e4
               [ord('i'),349.23],   #   f4
               [ord('o'),392],      #   g4
               [ord('p'),440],      #   a4
               [ord('a'),493.88],   #   b4
               [ord('s'),523.25],   #   c5
               [ord('d'),587.33],   #   d5
               [ord('f'),659.25],   #   e5
               [ord('g'),698.46],   #   f5
               [ord('h'),783.99],   #   g5
               [ord('j'),880],      #   a5
               [ord('k'),1760],     #   a6
               [ord('!'),69.30],    #   c2#
               [ord('@'),77.78],    #   d2#
               [ord('$'),92.5],     #   f2#
               [ord('%'),103.82],   #   g2#
               [ord('^'),116.54],   #   a2#
               [ord('*'),138.59],   #   c3#
               [ord('('),155.56],   #   d3#
               [ord('Q'),185],      #   f3#
               [ord('W'),207.65],   #   g3#
               [ord('E'),233.08],   #   a3#
               [ord('T'),277.18],   #   c4#
               [ord('Y'),311.13],   #   d4#
               [ord('I'),369.99],   #   f4#
               [ord('O'),415.30],   #   g4#
               [ord('P'),466.16],   #   a4#
               [ord('S'),554.37],   #   c5#
               [ord('D'),622.25],   #   d5#
               [ord('G'),739.99],   #   f5#
               [ord('H'),830.61],   #   g5#
               [ord('J'),932.33]])  #   a5#

final_audio_wave=[]
SineWave=[]

input_user=input("Enter all at once:")
for ip in input_user:
    if ip=='*':
        frequency=0
    else:
        for i in range(len(table)):
            if ord(ip)==table[i][0]:
                frequency=table[i][1]
                break
    sample_frequency=44100
    duration=1
    #noise=np.random.random_sample()
    #noise_amplitude=10
    #frequency=frequency+noise*noise_amplitude
    t=np.linspace(0,duration,sample_frequency*duration)
    phi=0
    amplitude=50
    SineWave=amplitude*np.sin(2*np.pi*frequency*t*sample_frequency+phi)
    concate_array(final_audio_wave,SineWave)
final_audio_wave=np.array(final_audio_wave,dtype=np.float32)   
wavfile.write('final.wav',sample_frequency,final_audio_wave)


