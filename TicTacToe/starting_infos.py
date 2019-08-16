class StartingInfos:
    """
        author: Noé Lüthold
        class: giving informations on how to play, at the start of the program.
    """

    def info(self):
        print("Author: Noé Lüthold")
        print("Last Updated: 14.08.2019")
        print("\n")
        print("It's recommended to play with the num-pad")
        print("\n")

    def instructions(self):
        instructionShow = input("Do you want to read the instructions? y/n")
        if instructionShow.lower() == "y" or instructionShow.lower() == "yes":
            print("Instructions:")
            print("TicTacToe is a game for two players, X and O, who take turns marking the spaces in a 3×3 grid.\n"
                  "The player who succeeds in placing three of their marks \n"
                  "in a horizontal, vertical, or diagonal row wins the game.\n\n")
            input("Press Enter to continue...")
