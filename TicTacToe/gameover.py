class Gameover:

    def overCheck(self, bL):
        if (bL[0][0] == " X " and bL[0][1] == " X " and bL[0][2] == " X ") or (
            bL[1][0] == " X " and bL[1][1] == " X " and bL[1][2] == " X ") or (
            bL[2][0] == " X " and bL[2][1] == " X " and bL[2][2] == " X "):
            return True

        elif (bL[0][0] == " O " and bL[0][1] == " O " and bL[0][2] == " O ") or (
              bL[1][0] == " O " and bL[1][1] == " O " and bL[1][2] == " O ") or (
              bL[2][0] == " O " and bL[2][1] == " O " and bL[2][2] == " O "):
            return True

        elif (bL[0][0] == " X " and bL[1][0] == " X " and bL[2][0] == " X ") or (
              bL[0][1] == " X " and bL[1][1] == " X " and bL[2][1] == " X ") or (
              bL[0][2] == " X " and bL[1][2] == " X " and bL[2][2] == " X "):
            return True

        elif (bL[0][0] == " O " and bL[1][0] == " O " and bL[2][0] == " O ") or (
              bL[0][1] == " O " and bL[1][1] == " O " and bL[2][1] == " O ") or (
              bL[0][2] == " O " and bL[1][2] == " O " and bL[2][2] == " O "):
            return True

        elif (bL[0][0] == " X " and bL[1][1] == " X " and bL[2][2] == " X ") or (
              bL[0][2] == " X " and bL[1][1] == " X " and bL[2][0] == " X "):
            return True

        elif (bL[0][0] == " O " and bL[1][1] == " O " and bL[2][2] == " O ") or (
              bL[0][2] == " O " and bL[1][1] == " O " and bL[2][0] == " O "):
            return True

        elif bL[0][0] != "   " and bL[1][0] != "   " and bL[2][0] != "   " and bL[0][1] != "   " and \
             bL[1][1] != "   " and bL[2][1] != "   " and bL[0][2] != "   " and bL[1][2] != "   " and bL[2][2] != "   ":
            return True

        else:
            return False
