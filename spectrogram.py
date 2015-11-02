'''
spectrogram.py
Frederik Roenn Stensaeth
11.01.15

A Python program that, when given a .wav. file name, will display a portion of
the spectrogram of that file.
'''

import numpy as np
import wave
import math
import struct
from PIL import Image
import sys
import os.path

def getFrequencyMagnitudes(trans_list):
    """
    getFrequencyMagnitudes() takes a list of fourier transform values and
    converts them to frequency magnitudes.
    
    @params: list of fourier transform values.
    @return: list of frequency magnitudes.
    """
    result = []
    
    for i in trans_list:
        # Takes the square root of the sum of the squares of the real and imag
        # parts of the fourier value.
        square_mag = (i.real ** 2 + i.imag ** 2) ** (0.5)
        
        # Converts the fourier value to log scale.
        log_sq_mag = 10 * math.log10(square_mag)
        
        result.append(log_sq_mag)
    
    return result

def printError():
    """
    printError() prints an error and usage message.
    
    @params: n/a.
    @return: n/a.
    """
    print('Error.')
    print('Usage: $ python3 spectrogram.py <wav sound file>')
    sys.exit()

def spectrogram(audio):
    """
    spectrogram() takes a .wav audio file name and creates a spectrogram for
    that file.
    
    @params: .wav file name.
    @return: n/a.
    """
    wavefile = wave.open(audio, 'rb')
    # wav files are 1 channel, 16bit samples. 16,000 Hz
    # 25ms windows and 10ms steps.
    # windows are 400 samples long and steps are 160 samples long.
    
    # Reads the data and puts it into a list.
    length = wavefile.getnframes()
    wavedata = []
    for i in range(0, length):
        data = struct.unpack('<h', wavefile.readframes(1))
        wavedata.append(data[0])
    wavefile.close()
    
    # Gets the window and step lengths.
    window_l = int(wavefile.getframerate() / 40) #400 # 25ms
    step_l = int(window_l / 2.5) #160 # 10ms
        
    # Gets the frequency magnitudes of the values for all the windows.
    # The frequency magnitudes is computed from the fourier values.
    freq_mag_list = []
    for i in range(0, length - window_l, step_l):
        frame = wavedata[i:i + window_l]
        freq_mag_list.append(getFrequencyMagnitudes(np.fft.fft(frame)))
    
    # Finds the max value we have seen.
    max_freq = float('-inf') #max(max(freq_mag_list))
    for row in freq_mag_list:
        max_freq = max(max_freq, max(row))
    
    # Creates a spectrogram of the frequency magnitudes by converting them to
    # a grayscale pixel value, where the max value we have seen is (0,0,0).
    image_pixel_lst = []
    for row in freq_mag_list:
        pixel_row = []
        for freq in row[:int(len(row) / 2)]:
            pixel_row.append([255 * (1 - (freq / max_freq))] * 3)
        image_pixel_lst.append(pixel_row)
    
    # Need to rotate the image 90 degress, as we want to swap the axis.
    image_pixel_lst = np.array(image_pixel_lst).astype('uint8')
    image_pixel_lst = np.rot90(image_pixel_lst, k = 1)
    
    visual = Image.fromarray(image_pixel_lst)
    visual.save(sys.argv[1] + '-spectrogram.jpg')
    visual.show()
    
def main():
    # Makes sure we have been given proper input.
    if len(sys.argv) != 2:
        printError()
    elif not os.path.isfile(sys.argv[1]):
        printError()
    elif sys.argv[1][-4:] != '.wav':
        printError()
    
    spectrogram(sys.argv[1])  

if __name__ == '__main__':
    main()