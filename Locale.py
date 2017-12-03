# Intro to Programming
# Author: Anthony Griggs
# Date: 11/27/17

#Define class Locale
class Locale:

    
    def __init__(self, sDescriptionPrim, sDescriptionSequ, index, tItems):
        self.sDescLong = sDescriptionPrim
        self.sDescShort = sDescriptionSequ
        self.i = index
        self.tItems = tItems
        self.bHasVisited = False
        self.bHasSearched = False
        self.tCanPickup = []
        for self.index in self.tItems:
            self.tCanPickup.append(False)
            
    def GetLocationDescription(self):
        if self.bHasVisited == True:
            return self.sDescShort
        return self.sDescLong

