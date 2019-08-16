from starting_infos import StartingInfos
from board import Board
from player import Player
from gameover import Gameover
from AI import AI


class Main:
    if __name__ == "__main__":
        infos = StartingInfos()
        p1 = Player()
        cB = Board()
        go = Gameover()
        ai = AI()

        infos.info()
        infos.instructions()

        while True:
            boardList = cB.createBoard()

            anotherGame = "yes"
            isPlayerTurn = True

            while True:
                cB.boardShowcase()
                cB.printBoard()

                if isPlayerTurn:
                    p1.playerTurn(boardList)
                    isPlayerTurn = False

                elif not isPlayerTurn:
                    ai.aiTurn(boardList)
                    isPlayerTurn = True

                IsGameOver = go.overCheck(boardList)

                if IsGameOver == 'X Won' or IsGameOver == 'O Won':
                    cB.printBoard()
                    print('\n')
                    print(IsGameOver)
                    anotherGame = input("Do you want to play another round? y/n ")
                    break

            if anotherGame.lower() != "y" and anotherGame.lower() != "yes" and anotherGame != "":
                break
