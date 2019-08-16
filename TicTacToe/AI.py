import random

# this class is responsible to write O's in random positions on the board and works as an adversary against the player
class AI:

    # this function generates 2 random numbers (0-2) and then checks if this field is free if it is, it places a O in it
    def aiTurn(self, board):
        # while no free square is found repeat the random number generation process
        while True:
            # generate the 2 random numbers
            x = random.randint(0, 2)
            y = random.randint(0, 2)

            # checks if the chosen square is empty or not, if it is it breaks out of the while loop
            if board[x][y] == "   ":
                break
        # prints the O
        board[x][y] = " O "
