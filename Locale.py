# Intro to Programming
# Author: Anthony Griggs
# Date: 11/27/17

#Define class Locale
class Locale:

    def __init__(self, sDescriptionPrim, sDescriptionSequ, tItems):
        self.sDescLong = sDescriptionPrim
        self.sDescShort = sDescriptionSequ
        self.tItems = tItems
        self.bHasVisited = False
        self.bHasSearched = False
