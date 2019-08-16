class Board:

    # setting the number of rows & columns and starting the first part of the array
    def __init__(self):
        self.boardList = ["   ", "   ", "   "]
        self.row = 3
        self.col = 3

    # Create the 2d array
    def createBoard(self):
        for y in range(self.row):
            self.boardList[y] = ["   "] * self.col
        return self.boardList

    # Creating a static board to indicate the buttons to press for every field.
    def boardShowcase(self):
        print("\n")
        print(" 7 | 8 | 9 ")
        print("---|---|---")
        print(" 4 | 5 | 6 ")
        print("---|---|---")
        print(" 1 | 2 | 3 ")
        print("\n")

    # Creating the chars around the board to make it look nice (the dividers etc.)
    def printBoard(self):
        boardStr = ""
        for x in range(self.row):
            for y in range(self.col):
                if y == self.col - 1:
                    boardStr += self.boardList[x][y]
                else:
                    boardStr += self.boardList[x][y] + "|"
            if x != self.row - 1:
                boardStr = boardStr + "\n---|---|---\n"
        print(boardStr)

