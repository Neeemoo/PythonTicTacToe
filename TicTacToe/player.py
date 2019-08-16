from board import Board
class Player:


    def playerTurn(self, boardList):
        while True:
            fieldInput = int(input("Write the number of an available square to set your symbol on it: "))
            if (fieldInput == 1):
                x = 2
                y = 0
            elif fieldInput == 2:
                x = 2
                y = 1
            elif fieldInput == 3:
                x = 2
                y = 2
            elif fieldInput == 4:
                x = 1
                y = 0
            elif fieldInput == 5:
                x = 1
                y = 1
            elif fieldInput == 6:
                x = 1
                y = 2
            elif fieldInput == 7:
                x = 0
                y = 0
            elif fieldInput == 8:
                x = 0
                y = 1
            elif fieldInput == 9:
                x = 0
                y = 2

            if fieldInput > 0 and fieldInput < 10 and boardList[x][y] != " X " and boardList[x][y] != " O ":
                boardList[x][y] = " X "
                print('\n')
                break
