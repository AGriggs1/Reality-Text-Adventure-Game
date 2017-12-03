# Intro to Programming
# Author: Anthony Griggs
# Date: 11/27/17

#Define class Player
class Player:
    #No parameters needed
    def __init__(self, pLocaleInit):
        self.pLocation = pLocaleInit
        self.iScore = 0
        self.iMoves = 0
        self.sName = "None"
        self.tInventory = []


