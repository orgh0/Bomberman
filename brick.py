import random
import time
import sys
from board import *
from random import randint
from termcolor import colored, cprint

class Brick():
	def __init__(self, obj):
		self.shape = ["/", "/", "/", "/", "/", "/", "/", "/"]
		self.x = self.y = 0
		while(obj.Matrix[self.x][self.y] != " "):
			self.x = (random.randint(1,100000000) % 16) * 2 
			self.y = (random.randint(1,100000000) % 16) * 4
		#print(self.x, self.y)
		for i in range (4):
			obj.Matrix[self.x][i + self.y] = colored(self.shape[i], 'yellow')
			obj.Matrix[self.x + 1][i + self.y] = colored(self.shape[i + 4], 'yellow')
