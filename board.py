from __future__ import print_function
import os
import sys
from termcolor import cprint, colored	

class Board():
	def __init__(self):
		self.Matrix = [[' ' for x in range(80)] for y in range(40)]
	
	def board_make(self):
		for i in range(34):
			for j in range(76):
				if(i < 2 or i > 31 or j < 4 or j > 71):
					self.Matrix[i][j] = "X"
				if ((i % 4 < 2 and j % 8 < 	4)):
					self.Matrix[i][j] = "X"
					
	def print_board(self):
		os.system("clear")
		for i in range(34):
			for j in range(76):
				cprint(self.Matrix[i][j],'red', end = " ")
			print()

