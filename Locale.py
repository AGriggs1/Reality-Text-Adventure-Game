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
        #self.ITEMS = tItems #WHY IS PYTHON STUPID?
        self.ITEMS = tItems
        self.DESC_LONG = sDescriptionPrim
        self.DESC_SHORT = sDescriptionSequ
        self.bHasVisited = False
        self.bHasSearched = False
        self.tCanPickup = []
        for self.index in self.tItems:
            self.tCanPickup.append(False)
        self.index = None
    def GetLocationDescription(self):
        if self.bHasVisited == True:
            return self.sDescShort
        return self.sDescLong

    def GetItemIndex(self, pItem):
        for self.index in range(len(self.tItems)):
            if self.tItems[self.index] == pItem:
                return self.index
        print("Item does not exist at this location!")
        return None

    def ResetValues(self):
        self.bHasSearched = False
        self.bHasVisited = False
        #self.tItems = self.ITEMS FOR WHATEVER REASON THIS MAKES IT SO THAT ONE
        #CHANGES THE OTHER DOES IN THE SAME. EXACT. WAY. PYTHON LOVES TO WASTE
        #MY TIME
        self.tItems = []
        for self.value in self.ITEMS:
            self.tItems.append(self.value)
        self.tCanPickup = []
        for self.index in range(len(self.tItems)):
            self.tCanPickup.append(False)
        
