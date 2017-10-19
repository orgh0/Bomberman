import sys
from termcolor import colored, cprint

class Bomb():
	def __init__(self, obj):
		self.planted =0
		self.x = 0
		self.y = 0
		self.timer = 3
		self.shape = ["@", "@", "@", "@", "@", "@", "@", "@"]
		self.blasted = 0;

	def print_bomb(self, obj, a, b):
		# if(obj.Matrix[a][b] == '['):
		for i in range (4):
			obj.Matrix[a][i + b] = colored(self.shape[i], 'cyan')
			obj.Matrix[a + 1][i + b] = colored(self.shape[i + 4], 'cyan')

	def blast(self, obj,enemy,player):
		print("blast")
		self.planted = 0
		self.timer = 3
		for i in range (5):
			obj.Matrix[self.x][i + self.y] = " "
			obj.Matrix[self.x + 1][i + self.y] = " "	
		for i in range (4):
			for j in range (4):
				if(obj.Matrix[self.x + i][self.y] != "X"):	
					obj.Matrix[self.x + i][self.y + j] = "$"
		for i in range(4):
			for j in range(4):
				if(obj.Matrix[self.x - i][self.y + j] != "X"):	
					obj.Matrix[self.x - i][self.y + j] = "$"
		for i in range(8):
			if(obj.Matrix[self.x ][self.y + i] != "X"):
				obj.Matrix[self.x + 1][self.y + i] = "$"
				obj.Matrix[self.x][self.y + i] = "$"
		for i in range (4):
			if(obj.Matrix[self.x][self.y - i] != "X"):	
				obj.Matrix[self.x + 1][self.y - i] = "$"
				obj.Matrix[self.x ][self.y - i] = "$"
		for i in range(5):
			if(enemy[i].x <= self.x+2 and enemy[i].x >= self.x-2 and enemy[i].y <= self.y+4 and enemy[i].y >= self.y-4):
				enemy[i].life = 0
		if(player.x <= self.x+2 and player.x >= self.x-2 and player.y <= self.y+4 and player.y >= self.y-4):
			player.lives -= 1
			player.x = 2
			player.y = 4
		self.blasted = 1

				


