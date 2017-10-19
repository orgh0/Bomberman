import random
from board import *
from brick import *
from bomb import *
from random import randint
import sys, time
from termcolor import colored, cprint

class Player():
	def __init__(self, obj):
		self.shape = ["B","B","B","B","B","B","B","B"]
		self.x = 2
		self.y = 4
		self.lives = 3
		self.print_player(obj)

	def check_piece_location(self, obj, a, b):
		# print (a,b)
		# print(obj.Matrix[a][b])
		if(obj.Matrix[a][b] == " " or obj.Matrix[a][b] == "B" or obj.Matrix[a][b] == "^" or obj.Matrix[a][b] == "[" or obj.Matrix[a][b] == "]"):
			return 1
		else:
			return 0

	def print_player(self, obj):
		if(obj.Matrix[self.x][self.y] == " "):
			for i in range (4):
				obj.Matrix[self.x][i + self.y] = colored(self.shape[i], 'green')
				obj.Matrix[self.x + 1][i + self.y] = colored(self.shape[i + 4], 'green')

	def motion(self, input, obj,obj1):
		if(input == 'q'):
			sys.exit(0);
		if(input == 'd'):
			print(obj.Matrix[self.x][self.y+4])

			if(self.check_piece_location(obj, self.x, self.y + 4)):
				self.clear(obj)
				self.y += 4
				self.print_player(obj)
		if(input == 'a'):
			print(obj.Matrix[self.x][self.y-4])

			if(self.check_piece_location(obj, self.x, self.y - 4)):
				self.clear(obj)
				self.y -= 4
				self.print_player(obj)
		if(input == 'w'):
			print(obj.Matrix[self.x-2][self.y])
			if(self.check_piece_location(obj, self.x - 2, self.y)):
				self.clear(obj)
				self.x -= 2
				self.print_player(obj)
		if(input == 's'):
			print(obj.Matrix[self.x+2][self.y])

			if(self.check_piece_location(obj, self.x + 2, self.y)):
				self.clear(obj)
				self.x += 2
				self.print_player(obj)
	  	if(input == 'x'):
			obj1.x = self.x
			obj1.y = self.y
			obj1.planted = 1

	def clear(self, obj):
		for i in range (4):
			obj.Matrix[self.x][i + self.y] = " "
			obj.Matrix[self.x + 1][i + self.y] = " "

class Enemy(Player):
	def __init__(self, obj):
		self.shape = ["^", "[","]","^"," ","]","["," "]
		self.x = self.y = 0
		self.life = 1
		
		while(obj.Matrix[self.x][self.y] != " "):
			self.x = random.choice(range(0,31,2))
			self.y = random.choice(range(0,71,4))

		if(obj.Matrix[self.x][self.y] == " " or obj.Matrix[self.x][self.y] == "$"):
			for i in range (4):
				obj.Matrix[self.x][i + self.y] = colored(self.shape[i], 'white')
				obj.Matrix[self.x + 1][i + self.y] = colored(self.shape[i + 4], 'white')

	def print_enemy(self, obj):
		if(obj.Matrix[self.x][self.y] == " " and self.life != 0):
			for i in range (4):
				obj.Matrix[self.x][i + self.y] = colored(self.shape[i], 'white')
				obj.Matrix[self.x + 1][i + self.y] = colored(self.shape[i + 4], 'white')

	def motion(self, obj):
		flag = random.randint(0, 4)
		retry = 4
		while(retry):
			if(flag == 0):
				if(self.check_piece_location(obj, self.x, self.y + 4)):
					self.clear(obj)
					self.y += 4
					self.print_enemy(obj)
					break
			elif(flag == 1):
				if(self.check_piece_location(obj, self.x, self.y - 4)):
					self.clear(obj)
					self.y -= 4
					self.print_enemy(obj)
					break
			elif(flag == 2):
				if(self.check_piece_location(obj, self.x - 2, self.y)):
					self.clear(obj)
					self.x -= 2
					self.print_enemy(obj)
					break
			elif(flag == 3):
				if(self.check_piece_location(obj, self.x + 2, self.y)):
					self.clear(obj)
					self.x += 2
					self.print_enemy(obj)
					break
			flag += 1
			flag %= 4
			retry -= 1
