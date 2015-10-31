'''
spectrogram.py
Frederik Roenn Stensaeth

A Python program that, when given a .wav file name, will display a portion of 
the spectrogram of that file.
'''

import sys

def printError():
	"""
	printError() prints an error and usage message.

	@params: n/a.
	@return: n/a.
	"""
	print('Error.')
	print('Usage: $ python3 spectrogram.py <wav file to be visualized>')
	sys.exit()

def spectrogram():
	"""
	"""
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