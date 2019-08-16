class StartingInfos:
    """
        author: Noé Lüthold
        class: giving informations on how to play, at the start of the program.
    """

    # this function prints out some basic onfromation about the program at the program start
    def info(self):
        print("Author: Noé Lüthold")
        print("Last Updated: 14.08.2019")
        print("\n")
        print("It's recommended to play with the num-pad")
        print("\n")

    # this function asks the user if he wants instructions on how to play and if he answers yes it prints it out
    def instructions(self):
        instructionShow = input("Do you want to read the instructions? y/n ")
        if instructionShow.lower() == "y" or instructionShow.lower() == "yes" or instructionShow == "":
            print("Instructions:")
            print("TicTacToe is a game for two players, X and O, who take turns marking the spaces in a 3×3 grid.\n"
                  "The player who succeeds in placing three of their marks \n"
                  "in a horizontal, vertical, or diagonal row wins the game.\n\n")
            # start with the game once he presses enter because we want to give him enough time to read it.
            input("Press Enter to continue...")
