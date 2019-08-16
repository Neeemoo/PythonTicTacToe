# PythonTicTacToe

This is almost an exact copy of the JavaTicTacToe, only in python, i did this to learn python a little better and then do some more difficult tasks with it.

#### main.py
This class communicates with the other classes and is the core of the application


#### starting_infos.py
Contains some basic informations like author etc. then askes the user if he wants to read the instructions.

#### board.py
This class contains the creation of the list used to then print the board.


#### player.py
Is responsible for ever step of the player turn from transforming the userinput to the numbers the program needs to understand it, to controlling if that square is empty, if it is it prints the X in it, if not it askes the user again.

#### gameover.py
Checks if a player won with 3 of their marks next to each other, if not it checks if the board is full ant it a draw.

#### AI.py
Basically it generates 2 random numbers between 0 and 2 and then it looks if the location is empty, if it is it places the O in it, if not it'll repeat until it is.
