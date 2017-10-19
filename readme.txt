This is a bomberman implementation done for the SSAD project of spring 2017.

Modules:
1.Board
2.Bomb
3.Brick
4.Game 

How to run :
Go to the directory via terminal and type ./game.py


Technical Details:

Work Flow :

[BOARD] -> board_make : initialised the board
        -> print_board : renders the board every iteration

[BOMB]
       -> print_bomb : saves the deployed bomb on the board
       -> blast : a function to blast the bomb

[BRICK] ->initalises the temporary brick

[GAME] wires all the function to make the workplay
