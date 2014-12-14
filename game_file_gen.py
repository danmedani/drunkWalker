#!/usr/bin/python

import random
import sys

height = int(sys.argv[1])
width = int(sys.argv[2])
chanceOfNum = float(sys.argv[3])
minVal = int(sys.argv[4])
maxVal = int(sys.argv[5])

for i in xrange(height):
	line = ''
	for j in xrange(width):
		if random.random() <= chanceOfNum:
			line = line + str(random.randint(minVal, maxVal)) + '|'
		else:
			line = line + '0|'
	line = line[:-1]
	print line