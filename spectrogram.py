'''
spectrogram.py
Frederik Roenn Stensaeth

A Python program that, when given a .wav file name, will display a portion of 
the spectrogram of that file.
'''

import sys
import os.path

def printError():
	"""
	printError() prints an error and usage message.

	@params: n/a.
	@return: n/a.
	"""
	print('Error.')
	print('Usage: $ python3 spectrogram.py <wav file to be visualized>')
	sys.exit()

def spectrogram(f):
	"""
	"""
	# Step 1: open wav file and get bytes.
	# Makes sure that we have been given a proper file to work with.
	try:
		f = wave.open(f, 'r')
		params = f.getparams()
		channels = params[0]
		width = params[1]
		rate = params[2]
		frames = params[3]

		byte_list = [] #f.readframes(frames)
		for i in range(frames):
			byte_list.append(f.readframes(1))

		f.close()
	except:
		printError()

	# Step 2: get windows
	frames_per_window = rate / 4 # 25ms
	step_size = rate / 10 # 10ms
	for start in range(0, frames, step_size)
		if start + frames_per_window < len(byte_list):
			window = byte_list[start:start + frames_per_window]

			Xx

	# Step 3: fourier transform --> numpy

	# Step 4: frequency magnitudes

	# Step 5: visualize

	return None

def visualizeFrequency(xx):
	"""
	"""
	return None

def getFrequencyMagnitudes(complex_list):
	"""
	"""

	# square and add

	# squareroot

	# 10 * log

	return None

def main():
	if len(sys.argv) == 2:
		spectrogram(sys.argv[1])
	printError()


if __name__ == '__main__':
	main()