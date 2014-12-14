#!/usr/bin/python

import sys
import random
import copy
import os
import time	

gameFile = sys.argv[1]
sleepTime = float(sys.argv[2])

with open(gameFile) as file:
    board = [[float(digit) for digit in line.split('|')] for line in file]

# print board

def getPieceList(b):
	pieceList = []
	# capture the actual pieces - less data to work with
	for i in xrange(len(b)):
		for j in xrange(len(b[i])):
			if b[i][j] != 0:
				tupe = i, j, b[i][j]
				pieceList.append(tupe)
	return pieceList

# print board
# print
# print pieceList

def xPos(p):
	return p[0]
def yPos(p):
	return p[1]
def valu(p):
	return p[2]
def nextXPos(p):
	return p[3][0]
def nextYPos(p):
	return p[3][1]

def nextX(piece, dir, dynBoard):
	if dir == 5 or dir == 6 or dir == 7:
		# move <- x
		return (len(dynBoard)-1) if xPos(piece) == 0 else xPos(piece) - 1
	elif dir == 1 or dir == 2 or dir == 3:
		# move x ->
		return 0 if xPos(piece) == (len(dynBoard)-1) else xPos(piece) + 1
	else:
		return xPos(piece)

def nextY(piece, dir, dynBoard):
	if dir == 3 or dir == 4 or dir == 5:
		# move <- y
		return (len(dynBoard[0]) - 1) if yPos(piece) == 0 else yPos(piece) - 1
	elif dir == 0 or dir == 1 or dir == 7:
		# move y ->
		return 0 if yPos(piece) == (len(dynBoard[0])-1) else yPos(piece) + 1
	else:
		return yPos(piece)

def pPr(b):
	for row in b:
		stLine = ''
		for val in row:
			stLine = stLine + '{0: <5}'.format(str(int(val)))
		print stLine
	print

count = 0
pList = getPieceList(board)
while len(pList) > 1:
	pList = getPieceList(board)
	count = count + 1
	newPlist = []
	for piece in pList:
		randoDir = random.randint(0, 7)
		nextPos = nextX(piece, randoDir, board), nextY(piece, randoDir, board)

		# Add next piece spot
		newPlist.append(piece + (nextPos,))

	# update board
	for piece in newPlist:
		board[xPos(piece)][yPos(piece)] = board[xPos(piece)][yPos(piece)] - valu(piece)
		board[nextXPos(piece)][nextYPos(piece)] = board[nextXPos(piece)][nextYPos(piece)] + valu(piece)

	os.system('clear')
	print count
	print len(pList)
	print
	pPr(board)
	time.sleep(sleepTime)

	# pPr(board)
	# print
	# print pList



