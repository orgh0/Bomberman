#!/usr/bin/env python
from __future__ import print_function
from board import *
from player import *
from getchunix import *
from alarmexception import *
from bomb import *
import sys,time
from termcolor import colored, cprint
getch = GetchUnix()

def alarmHandler(signum, frame):
	raise AlarmException

def input_to(timeout = 1):
	signal.signal(signal.SIGALRM, alarmHandler)
	signal.setitimer(signal.ITIMER_REAL, timeout)
	try:
		text = getch()
		signal.alarm(0)
		return text
	except AlarmException:
		print("\n Prompt timeout. Continuing...")
	signal.signal(signal.SIGALRM, signal.SIG_IGN)
	return ''

bomb_temp = 0
board = Board()
board.board_make()
player = Player(board)
brick_count = 25
brick = []
for i in range(brick_count):
	brick.append(Brick(board))
enemy_count = 5;
enemy = []
count = 0
bomb = Bomb(board)
#bomb.print_bomb(board, 2, 8)
for i in range(enemy_count):
	enemy.append(Enemy(board))
while(player.lives):
	if(bomb.blasted == 1):
		# print("taest")
		for i in range(34):
			for j in range(76):
				if (board.Matrix[i][j] == "$"):
					board.Matrix[i][j] = " "
		bomb.blasted = 0
	for i in range(enemy_count):
		enemy[i].motion(board)
	c = input_to()
	player.motion(c, board,bomb)
	for i in range(enemy_count):
		if(enemy[i].x == player.x and enemy[i].y == player.y):
			player.lives -= 1
			player.x = 2
			player.y = 4
	if (bomb.planted == 1 and (player.x != bomb.x or player.y != bomb.y)):
		bomb.print_bomb(board , bomb.x , bomb.y)
	if(bomb.planted == 1):
		bomb.timer -= 1
	if(bomb.timer == -1):
		bomb.blast(board,enemy,player)
	board.print_board()
	print("Lives:" , player.lives)
