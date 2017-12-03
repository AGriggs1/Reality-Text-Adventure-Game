# Intro to Programming
# Author: Anthony Griggs
# Date: 9/12/17

#Project4
#Ver 0.7 11/8/17

from time import sleep # :) Only once
import sys #Learned about this from https://stackoverflow.com/questions/949504/terminating-a-python-program
from Locale import *
from Player import *
          
cont = "<Press enter to "
bDevMode = True
pVoidDummy = Locale("You find yourself in an empty white space, a 'nothing'.", None, 0, [])
pVoid = Locale("You are in an empty white space. A red circle with four lines leading in four directions"
               "to four other circles appears under your feet.",
               "You are in the center of the void.", 1, ["BlockN, BlockS, BlockE, Blockw"]) #For now, I just want to define every location, so I'll just list the name of the item.

pVoidN = Locale("You follow one of the lines to a circle that, upon investigation, has the letter 'N' on it."
                "The area around you transforms into a forest filled teeming monstrous redwood trees."
                "You hear the songs of various birds, and feel welcome.",
                "You return to the forest", 2, [])

pVoidS = Locale("You follow one of the lines to a circle that, upon investigation, has the letter 'S' on it."
                "The area around you transforms. Suddenly you are at the edge of a cliff overlooking the open sea."
                "You hear the waves crashing against the crags below you, smell the mist of saltwater, and feel a sense of somberness.",
                "You return to the cliffside", 3, [])

pVoidE = Locale("You follow one of the lines to a circle that, upon investigation, has the letter"
                "'E' on it. The area around you transforms and you are on the streets of a city that seems to be long abandoned. "
                "Cars rusted, buildings crumbling, overgrown with moss and vines. You can't help but feel curious about the fate of this place.",
                "You return to the city ruins", 4, [])

pVoidW = Locale("You follow one of the lines to a circle that, upon investigation, has the letter 'W' on it. "
                "The area around you transforms into an office."
                "Desks teeming with paperwork and the faint smell of morning coffees makes you anxious.",
                "You return to the office", 5, [])

pCloset = Locale("You are in a broom closet. The shelves are littered with various objects. Perhaps there is something of use?",
                 "You're in a broom closet.", 6, ["Flashlight", "Matches", "Hammer"])

pHallway1 = Locale("You walk down a hallway and come to a corner.",
                   "You are at a hallway corner. ", 7, ["Map"])

pOfficeNW = Locale("You enter one of the office corners. Papers and supplies litter the floor.",
                   "You enter the Northwest corner of the office.", 8, [])

pOfficeW = Locale("You come to a large room full of cubicles, cubicles, cubicles. The building you're in must be an office, then.",
                  "You are in the office.", 9, [])

pOfficeSW = Locale("You enter one of the office corners, which has a particuliarly large ficus. You study it with intensity.",
                   "You enter the Southwest corner of the office.", 10, ["Batteries"])
                   
pOfficeN = Locale("You enter a cubicle that is larger than all the rest. It looks like it's supposed to fit 4, maybe 5 people. "
                  "The thought makes you feel claustrophobic.", "You are in the large cubicle.", 11, [])
pOfficeC = Locale("You enter the center of the office, the center of the universe.", "You are in the center of the office.", 12, [])

pOfficeS = Locale("You find a pair of doors. What lies beyond them?", "You head towards the double doors.", 13, [])

pOfficeNE = Locale("You enter on the office corners. There is a water cooler, but's its empty.", "You are in the Northeast corner of the office.", 14, [])
                   
pOfficeE = Locale("You are now on the other side of the office. Something feels off, or perhaps you're just sick of this place.",
                   "You are in the the office. ", 15, [])

pOfficeSE = Locale("You enter one of the office corners. There is a painting of a sad clown. What?",
                   "You're in the Southeast corner of the office.", 16, [])

pHallway2 = Locale("You walk down a hallway, and come to a corner.", "You are at a hallway corner. ", 17, [])

pForest = Locale("You come to a door. Upon opening it you suddenly find yourself in a forest. "
                "You enter, and as you look behind you, you find all traces of the office building to be gone."
                " All you see are trees, but you can hear the sound of running water.",
                 "You are in the forest. ", 18, ["Rope"])

pLake = Locale("You follow the river to a large lake. It's shores are sandy, interestingly enough.", "You return to the lake.", 19, ["Idol"])

pRiver = Locale("You come to a river bank. You faintly hear what sounds like constant thunder.", "You are at the river.", 20, [])

pWaterfall = Locale("You follow the river to a waterfall. It looks like it's about 15 feet high, but what do you know?", 
                "The waterfall stands before you. Lovely.", 21, [])

pCaveEnt = Locale("Behind the waterfall you find an entrance to a cavern. What lies within?",
                  "You are behind the waterfall, at the maw of a cavern.", 22, [])

pCave = Locale("You go down into cave. It's pitch black, and you walk slowly and with caution. ",
               "You are within the dark cavern. ", 23, [])

pCaveDeep = Locale("You go deeper into the cave. You come to an empty chamber with a small opening to the surface, allowing you to see.",
                   "You are deep within the cave", 24, ["Key"])

pRavine = Locale( "You take a step forward, not knowing there is nowhere to place your foot. "
                "Suddenly, you find yourself tumbling down, down, down..."
                " You hit the bottom of the ravine. Hard. You cannot see how broken you are, but you know it's bad. "
                "You begin to lose consciousness.", "You are at the bottom of a ravine", 25, [])
                 
pWaterfallTop = Locale("Following the current, you come across the top of a waterfall. It looks like a 15-foot drop, but what do you know?",
                       "It's the top of a waterfall. Again.", 26, ["I might put something here"])





#Navigation Matrix
mLocations = [
        #c0-3 = N, S, E, W
        ##===FIRST MAP=========##
        [None, None, None, None],   #-------------r0 - VoidM (Intro)
        [pVoidN, pVoidS, pVoidE, pVoidW], #-----------r1 - VoidM
        [None, pVoid, None, None], #--------------r2 - VoidN
        [pVoid, None, None, None], #--------------r3 - VoidS
        [None, None, None, pVoid], #--------------r4 - VoidE
        [None, None, pVoid, None], #--------------r5 - VoidW
        ##===SECOND MAP========##
        [pHallway1, None, None, None], #---------------r6 -- Closet
        [None, pCloset, pOfficeW, None], #-------------r7 -- Hallway1
        [None, pOfficeW, pOfficeN, None], #------------r8 -- OfficeNW
        [pOfficeNW, pOfficeSW, pOfficeC, pHallway1], #-r9 -- OfficeW
        [pOfficeW, None, pOfficeS, None], #------------r10 - OfficeSW
        [None, pOfficeC, None, pOfficeNW], #-----------r11 - OfficeN
        [pOfficeN, pOfficeS, pOfficeE, pOfficeW], #----r12 - OfficeC
        [pOfficeC, None, pOfficeSE, pOfficeSW], #------r13 - OfficeS
        [None, pOfficeE, None, None], #----------------r14 - OfficeNE
        [pOfficeNE, pOfficeSE, pHallway2, pOfficeC], #-r15 - OfficeE
        [pOfficeE, None, None, pOfficeS], #------------r16 - OfficeSE
        [None, pForest, None, pOfficeE], #-------------r17 - Hallway2
        [None, pRiver, None, None], #------------------r18 - Forest
        [pForest, None, pWaterfall, pLake], #----------r19 - River
        [None, None, pRiver, None], #------------------r20 - Lake
        [None, None, pCaveEnt, pRiver], #--------------r21 - Waterfall
        [None, pCave, None,pWaterfall], #-------------r22 - CaveEnt
        [pCaveEnt, pRavine, None, pCaveDeep], #--------r23 - Cave
        [None, None, None, None], #---------------------r24 - CaveDeep
        [None, None, None, None], #--------------------r25 - Ravine(Hidden location, does not appear on map. Eventually the entire cave system won't appear on the map)
        [None, None, pRiver, pWaterfall] #-------------r26 - WaterfallTop(replaces lake)
            ]
sRavine = "With your source of light, you see a large drop-off to the south side. You can't see the bottom from here." #I'm not sure you can use other parts of a list when defining a list.

#Define examine results
sNoUse = "You see nothing of use."
tLocationsExamine = [           #Examine is dual purpose. It prints the index of this list based on location index and it checks if the location has an item
                #0 - None
                None,
                #1 - VoidM, None
                sNoUse,
                #2 - VoidN, Doll
                sNoUse,
                #3 - VoidS, None
                sNoUse,
                #4 - VoidE, None
                sNoUse,
                #5 - VoidW, None
                sNoUse,
                #6 - Closet, Map
                "On one of the shelves you find what looks like some sort of map.",
                #7 - Hallway, None
                sNoUse,
                #8 - OfficeNW, None
                "You rumage through the various papers and see nothing particuliarly interesting. Wait! Oh. Nevermind.",
                #9 - OfficeW, None
                sNoUse,
                #10 - OfficeSW, Flashlight
                "You look in the plant pot, and see what looks like a flashlight.",
                #11 - OfficeN, None
                "You try turning on one of the cubicle computers. It boots instantly to a text document that reads:\n"
                "\n'The sun sets, the water chasing it\n\nWhere they meet the secret of their journey shall be revealed'",
                #12 - OfficeC, None
                sNoUse,
                #13 - OfficeS, None
                "The doors simply won't budge. Is there a key somewhere?", #No
                #14 - OfficeNE, None
                "Just an empty watercooler. What a shame.",
                #15 - OfficeE, None
                sNoUse,
                #16 - OfficeSE, None
                "The portrait has an inscription. It reads 'Chairman Bobbo the Clown, may he grace you with his gaze.' Yeah-huh.",
                #17 - Hallway, None
                "You don't see anything.", #Very subtle way to tell the difference between hallways
                #18 - Forest, Rope (In the future, this combined with the flashlight will let you safely explore the ravine
                "Among the trees you see some sort of rope.",
                #19 - River, None
                "Just a river here, nothing to see.",
                #20 - Lake, Idol
                "Along the lake shores you find some sort of small wooden figureine.",
                #21 - Waterfall, None
                sNoUse,
                #22 - Cave Entrance, None
                sNoUse,
                #23 - Cave, None
                sNoUse,
                #24 - Deep Cave, None
                sNoUse,
                #25, Ravine
                None,
                #26, WaterfallTop
                sNoUse
                ]
#Define items
pDoll = "Doll"
pMap = "Map"
pFlashlight = "Flashlight"
pHammer = "Hammer"
pRope = "Rope"
pIdol = "Idol"
tLocationsItem = [
                #0 - Void
                None,
                #1 - VoidM
                None,
                #2 - VoidN
                None, 
                #3 - VoidS
                None,
                #4 - VoidE
                None,
                #5 - VoidW
                None,
                #6 - Closet
                pMap,
                #7 - Hallway
                None,
                #8 - OfficeNW
                None,
                #9 - OfficeW
                None,
                #10 - OfficeSW
                pFlashlight,
                #11 - OfficeN
                None,
                #12 - OfficeC
                None,
                #13 - OfficeS
                None,
                #14 - OfficeNE
                None,
                #15 - OfficeE
                None,
                #16 - OfficeSE
                None,
                #17 - Hallway
                None,
                #18 - Forest
                pRope,
                #19 - River
                None,
                #20 - Lake
                pIdol,
                #21 - Waterfall
                None,
                #22 - Cave Entrance
                None,
                #23 - Cave
                None,
                #24 - Deep Cave
                None,
                #25 - Ravine
                None,
                #26 - WaterfallTop
                None
                ]

                
#Define table that holds booleans for whether or not the player has visited certain locations
tVisited = []
#For each location, append a False boolean to start with
#for i in tLocationsShort:
#    tVisited.append(False)
#Create a copy of tVisited that will act as a check as for whether or not the player can be pickup any item at a location
#tCanPickup = tVisited




##=============================================================    
def Init(): #Initialization function, runs when the code is run
            #Delete irrelevant comments you mong
##=============================================================
    #tInventory = []
    #iScore = 0
    pPlayer = Player(pVoidDummy)
    sTitle = ( "*********   *********      ***      *           *********   *********   *       *\n" 
               "*       **  *              * *      *               *           *        *     *\n"
               "*        *  *             ** **     *               *           *         *   *\n"
               "*       **  *             *   *     *               *           *          * *\n"
               "*********   *********    *******    *               *           *           *\n"
               "*       **  *            *     *    *               *           *           *\n"      
               "*        *  *           **     **   *               *           *           *\n"           
               "*        *  *********   *       *   *********   *********       *           *\n")           #Dios ayudame si yo decido hacer un titulo nuevo.
    print(sTitle)
   # pLocation, iNumMoves, iScore = SetLocation("None", iVoidStart, 0, 0)
    #pLocation = tLocationsLong[0] #The traditional way won't work for initializing locations, since SetLocation now requires the location you're currently at to work
                                 #That means it more than likely will not work for forcing a location via interpret
    #Begin introduction
   # pPlayer = Player(pLocation)
    print(pPlayer.pLocation.sDescLong) #Needs to be cleaned up, naturally    
    sInput = input("input: ") or "None"  #If sInput is None (player hits enter without typing anything) then fill it in with "None"

    
    sInput, sName = Interpret(sInput, None, 0, 0, "Init") #Hmmmm
    if sInput:
        print("???: Hey! Can you hear me?")
        input(cont + "continue>") #Must use concatenation for input
    
        print("???: Good. Now, I know you must have plenty of questions, such as where you are, or who I am. We'll get to them when the time comes.\n\n"
              "???: There are more pressing matters. Protocol insists that I perform a sitrep on your state of being before we can address any inquiries.\n"
              "Understand?")
    
        input(cont + "understand>")
        #Get player name
        sName = input("???: First things first: do you know your name?\nYour name? ")
    
        print("???: " + sName + "? All right. Now let's see about your sense of orientation.\n")
        print("Suddenly a red circle appears beneath your feet. You notice four lines spreading outward from it in four directions,"
              " leading to other circles\n")
        print("???: Okie-dokie, go ahead and walk towards any of these circles. I know you're confused, but stick with me."
              " If you feel you need help, just say the word.\n")
        print("<Type 'North', 'South', 'East', or 'West' to head in that direction. To see all commands availible to you, type 'Help'>\n")
    
        #Update pLocation to showcase changes made
        pPlayer.pLocation = pVoid
        #Enter the gamestate for the first time
        Main(pPlayer)
        #Begin second half of intro
        print("\n???: Excellent, " + sName + ". You seem to be in optimal shape. Excellent indeed.\n"
              "You're patience with me has not gone unnoticed. I... do not have not been aquainted."
              " I am Bx106001-c. I am a Generation IV Class C Artificial Intelligence. You may call me Baby.\n"
              "Baby: I know you are curious as for where you are, but that's a bit more difficult. "
              "Could you define what exactly you wish to know about your whereabouts?\n")
    
        input() #Hm, is Baby decieving you?
        print("Baby: ERROR: Acess denied.")
        sleep(1)
    
        for i in range(150):
            print("x003334" + str(i) + ".FATAL: Bx106001-c Gen IV 'Bravo-Alfa-Bravo-Yankee'"
                  " has @#4uNt2#d an is$3@ that has co#$Afg0sed *&ad$%3-sufficient operations!")
            #Baby has ecountered an issue that has compromised self-sufficient operations!

        print("Baby: Oops! Looks I had a little hiccup there.\n"
              "Baby: I'm sorry, but you don't have permission to access such information without the correct access code."
              " Please input access code now.")
        #Hmmm, maybe I could add a little easter egg here
        sInput = input("Access code: ")
    
        print("Baby: Nuh-uh. Wrong, as expected. Hm, tell you what, I'll at least tell you what you're here for."
              " This place, whatever it may be to you, is to test your physical and cognitive abilities.\n"
              "Baby: I... am to test you. You pass this, and Baby will tell you anything.\n"
              "I may even let you go free!\n"
              "...") #In the future, 'Baby:' should be a var
    
        input(cont + "question Baby>")
        print("Baby: This test is not optional! You're going to participate and you're going to love it! You'll see...\n"
              "Baby: Let's start!")
    #Block Cave
    ReplaceLocation(iWaterfall, 2, None)
    pLocation = tLocationsLong[iCloset]
    tVisited[iCloset] = True
    pLocation, iScore, tInventory = Main(pLocation, sName, iScore, 0, tInventory)
    Copyright(iScore, True)
##
##====================================
#GetLocationDescription
#Returns the long or short description of defined location
##====================================
def GetLocationDescription(self):
    if pLocation.bHasVisited == True:
        return pLocation.sDescShort
    return pLocation.sDescLong

##========================================
#DoesHaveItem    
#Determines if the player has the defined item
##========================================
def DoesHaveItem(pItem, pPlayer):
    #Check the inventory for the defined item
    for p in pPlayer.tInventory:

        if p == pItem:
            return True
    #Not found in table
    return False
##
#CanPickup
#Checks if the player can pickup the defined item
##

##======================================
#Pickup
#Gives the player the item at sLocation
##======================================
def Pickup(pPlayer, pItem):
    
    index = pPlayer.pLocation.i
    pLocation = pPlayer.pLocation
    for i in pLocation.tItems:
        if pLocation.tItems[i] == pItem and pLocation.tCanPickup[i]:
             pPlayer.tInventory.append(pItem)
             pLocation.tItems[i] = None
             tLocationsExamine[i] = None
                
    #i = GetLocation(sLocation)
    
    #pItem = tLocationsItem[i]
    
    #if  tCanPickup[i] and pItem is not None:
        #tPlayerInventory.append(pItem)
        #print("Picked up the", pItem + ".")
        #Remove the item from the examine list, but NOT the item list since that will break DoesHaveItem
        #tLocationsExamine[i] = sNoUse 
        #return tPlayerInventory
    #print("Nothing to pickup.")
    #Set location as visited
    #tVisited[i] = True
    #return tPlayerInventory 
##==============================================
#SetLocation
#Sets the player's location
#Parameters:
    #sLocation, the player's current location
    #iTo, the index of the location the player is moving to
    #iMoves, the number of moves
##==============================================
def SetLocation(pPlayer, iDirection):
    #iTo = mLocations[GetLocation(sLocation)][iDirection] or GetLocation(sLocation) #if going that direction is None

    if mLocations[pPlayer.pLocation.i][iDirection] == None:
        print("You can't go that way")
        return pPlayer.pLocation

    pPlayer.pLocation = mLocations[pPlayer.pLocation.i][iDirection]
    if not pPlayer.pLocation.bHasVisited:
        pPlayer.iScore += 5
    #    pPlayer.pLocation.bHasVisited = True
    pPlayer.iMoves += 1
    return pPlayer.pLocation
        
    #if sLocation == tLocationsLong[iTo] or sLocation == tLocationsShort[iTo]:
        #print("You can't go that way")
        #return sLocation, iNumMoves, iScore

    #print(iTo)
    #sLocation = tLocationsLong[iTo]

    #if not tVisited[iTo]:
        #Use short description table instead
        #iScore = iScore + 5
        #tVisited[iTo] = True

    #else:
        #sLocation = tLocationsShort[iTo]
    #iNumMoves = iNumMoves + 1
    #return sLocation, iNumMoves, iScore

#def GetLocation(sLocation):
    # pass
    #for i in range(len(tLocationsShort)): #The length should be the same
        
        #if tLocationsShort[i] == sLocation:
            #return i
        
        #if tLocationsLong[i] == sLocation:
            #return i
    #print("Error: pLocation not found")
    #return None
##==================================
#SwitchLocations
#Takes two rows(location) and two columns(direction) and switches their place on the navigation matrix
##==================================
def SwitchLocations(r1, c1, r2, c2):
    iLocation = mLocations[r1][c1]
    mLocations[r1][c1] = mLocations[r2][c2]
    mLocations[r2][c2] = iLocation

##======================================
#ReplaceLocation
#Takes a row and column and replaces it with iLocation
##======================================
def ReplaceLocation(r, c, iReplaceWith):
    mLocations[r][c] = iReplaceWith

##================================
#Copyright
#Prints the copyright/gameover statement
#Parameters:
    #iScore, the player's score
    #bGameover, used to determine if the gameover statement should be printed
##================================
def Copyright(pPlayer, bGameover):
    sMessage = "Copyright Anthony Griggs. Email inquiries to Anthony.Griggs1@marist.edu"

    if bGameover:
        print("Final score:", pPlayer.iScore)
        print("Gameover!\nThanks for playing!\n " + sMessage)
        sys.exit()
    print(sMessage)

#Used for a dev command
#Lower case since Interpret makes use of .lower()
#In hinesight I could have done something like "string".lower() and kept everything readable 
gDevKeys = {
            "voidm"     :0,
            "voidmreal" :1,
            "voidn"     :2,
            "voids"     :3,
            "voide"     :4,
            "voidw"     :5,
            "closet"    :6,
            "hallway1"  :7,
            "officenw"  :8,
            "officew"   :9,
            "officesw"  :10,
            "officen"   :11,
            "officec"   :12,
            "offices"   :13,
            "officene"  :14,
            "officee"   :15,
            "officese"  :16,
            "hallway2"  :17,
            "forest"    :18,
            "river"     :19,
            "lake"      :20,
            "waterfall" :21,
            "caveent"   :22,
            "cave"      :23,
            "deepcave"  :24
            }
##==========================================
#Interpret
#Takes user input and decides what to do
#Parameters:
#   sInput, the player input to read
#   pLocation, the player's location
#   iScore, the player's score
#   iNumMoves, the player's moves
#   FunctionFrom, the function Interpret is being called from. This will likely be a short string
#
#The parameters required will be a lot less once objects are used
#   
##==========================================
def Interpret(sInput, pLocation, iScore, iNumMoves, FunctionFrom): #Parameters can be reduced once the player becomes an object with methods that can get these for us
    sInput = sInput.lower()
    sNone = "None"
    s = "Interpret:"
    #If sInput was empty, just end
    if sInput == "none":
        return True, sInput
    ##===============
    #Special commands (where they can be used will depend on the command)
    ##===============
        #therefore, what they return depends on FunctionFrom
    if bDevMode and sInput[0:4] == "dev:":
        print(s, "Developer mode active. Developer command detected.")
        sInput = sInput[4:len(sInput)] #Go ahead and cut off the first 'dev:' since we already checked that
        print(s, "Command is", sInput)
        
        try:
            sInput, sArg = sInput.split() #Split sInput by white spaces if needed
        except:
            print("sInput does not need to be split")
        ##WILL NOT WORK THIS VERSION
        if sInput == "setlocation" and FunctionFrom == "Main":

            try:
                print(sArg)
                i = gDevKeys[sArg] #Find the location using the split sArg and the special dictionary
                pLocation, iNumMoves, iScore = SetLocation("Irrelevant", i, iNumMoves, iScore) 
            except:
                print("Error: key not found")
           
            return True, pLocation, None, iNumMoves, iScore, "setlocation"
        
        #TODO: If statements for commands go here
    ##=====================    
    #Valid commands in Init
    ##=====================
        #returns a boolean and a string
    if FunctionFrom == "Init":
        if sInput.lower() == "skip":
            sInput = input("???: Hey, hey, what do you think you're doing trying to skip my glorius introduction,"
                           " bub? Do you even know my name? ")

            if sInput.lower() == "baby":

                print("Baby: ...")
                sInput = input("Baby: Fine! What's you're name, dum-dum?")
                return False, sInput  #May change the return values in the future
            else:
                print("???: Hmph! Hm hm! HM HM HM HM! Let's reimmerse ourselves, yeah? *Ahem*")
                return True, "It's Baby"
        return True, "What?"
    #Consider spliting up a string by spaces and interpreting every word in it
    ##=====================
    #Valid commands in Main
    ##=====================        
                #returns a boolean, then two strings, then two ints, then another string
    elif FunctionFrom == "Main":
        if sInput == "north":
            pass
            #return pLocation, None, iNumMoves, iScore, "setlocation"

        elif sInput == "south":
            pass
            #return ditto
        elif sInput == "east":
            pass
            #return ditto
        elif sInput == "west":
            pass
            #return ditto

        elif sInput == "help":
            print(gHelp) #I feel globals are okay IF they are intended to not be changed by the program
            return True, None, None, None, None, None #Nothing to distribute
        elif sInput == "quit":
            sInput = input("This will end the game and count as a game over. Continue?\n" #Changing sInput shouldn't cause issues
                  "<Enter 'y' for 'yes or 'n' for no'>\n")
            sInput = sInput[0].lower()

            if(sInput == "y"):
                Copyright(iScore, True)
            return True, pLocation, None, iNumMoves, iScore, "quit exempt"
            
    return True, pLocation, None, iNumMoves, iScore, "failed"  #Input could not be interpreted
    #Todo: Insert function into main where necessary
##============================
#UpdateLocation
#Simple function that checks if the game should use the short description
##============================
def UpdateLocation(pPlayer):
    if not pPlayer.pLocation.bHasVisited:
        pPlayer.pLocation.bHasVisited = True
    #i = GetLocation(pLocation)
    #if tVisited[i] == True:
        #return tLocationsShort[i]
    #return pLocation

def GenerateMap(Map, MapDescription, tMap, bDoRegenerate):
    if bDoRegenerate:
        #Get the Nav Matrix Sequence (Map one is r0-5, Map two is r6-25)
        #Wipe Map Matrix (set everything to NA)
        #Try to interpret how its currently put together
        #Redesign Grid to match
        pass
    for r in Map:
        s = ""
        for c in r:
            #c = c + c
            s = s + c
        print(s)
    print(Map) #Remove in future
    print(MapDescription)
    return Map
##===========================================
#Main
#Gamestate function, always active while player is in the game
#Parameters:
#   *sLocation, the location to start the game at
#   *sName, the name the player chose
#   *iScore, the player's score at this point of the game
#   *tPlayerInventory, the player's inventory
##============================================
sNoGo = "You can't go that way."
gMapTut = ("   N    \n"
           "   |    \n"
           "W--M--S \n"
           "   |    \n"
           "   S    \n")

gMap = ("   c1--C   c6           \n"
        "   |   |   |             \n"
        "b--c2--c4--c7--d         \n"
        "|  |   |   |   |         \n"
        "a  c3--c5--c8  e         \n"
        "               |         \n"
        "            g--f--h--i   \n"
        "                     |   \n"
        "                  k--j   \n")



NA = "  "
HD = "--"
VD = "| "
N_ = "N "
S_ = "S "
E_ = "E "
W_ = "W "
a_ = "a "
b_ = "b "
c1 = "c1"
c2 = "c2"
c3 = "c3"
cC = "C "
c4 = "c4"
c5 = "c5"
c6 = "c6"
c7 = "c7"
c8 = "c8"
d_ = "d "
e_ = "e "
f_ = "f "
g_ = "g "
h_ = "h "
i_ = "i "
j_ = "j "
k_ = "k "
l_ = "l "
m_ = "m "
n_ = "n "
o_ = "o "
        
#Beginning to experiment with mutable map
#This is going to be a coordinate grid
mMap = [
        [NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA], 
        [NA, NA, c1, HD, cC, NA, c6, NA, NA, NA, NA, NA, NA, NA],
        [NA, NA, VD, NA, VD, NA, VD, NA, NA, NA, NA, NA, NA, NA],
        [b_, HD, c2, HD, c4, HD, c7, HD, d_, NA, NA, NA, NA, NA],
        [VD, NA, VD, NA, VD, NA, VD, NA, VD, NA, NA, NA, NA, NA],
        [a_, NA, c3, HD, c5, HD, c8, NA, e_, NA, NA, NA, NA, NA],
        [NA, NA, NA, NA, NA, NA, NA, NA, VD, NA, NA, NA, NA, NA],
        [NA, NA, NA, NA, NA, NA, g_, HD, f_, HD, h_, HD, i_, NA],
        [NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, VD, NA],
        [NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, k_, HD, j_, NA],
        [NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA]
        ]


        


gMapDesc = ("a = Closet\n"
            "b = Hallway Corner\n"
            "Cc = Office\n"
            "d = Other Hallway Corner\n"
            "e = Forest\n"
            "f = River\n"
            "g = Lake\n"
            "h = Waterfall\n"
            "i = Cave Entrance\n"
            "j = Cave\n"
            "k = ???")

#m = GenerateMap(mMap, gMapDesc, None, False)
tMap = ["Error: Could not determine location", "M", "N", "S", "E", "W", "a", "b", "c1", "c2", "c3",
        "C", "c4", "c5", "c6", "c7", "c8", "d", "e", "f", "g", "h", "i", "j", "k"]
#Since the location at 0 is not used in the game loop, it can be used to display an error message
#But for now we'll stick with the is not None check

def Main(pPlayer):
    bGameState = True
    bDoShowSequence = True
    
    while bGameState:
     #   bHasLight = DoesHaveItem(pFlashlight, tPlayerInventory)
        print(pPlayer.pLocation.GetLocationDescription())
        #Update pLocation
        UpdateLocation(pPlayer)
        sInput = input()
        sInput = sInput.lower()
        #bVar1, sVar1, sVar2, iVar1, iVar2, sResult = Interpret(sInput, pLocation, iScore, iNumMoves, "Main")#This is going to get hideous
        #Now we just need to interpret the return values here by looking at sResult
        #if sResult is not none:
        #   if sResult is "setlocation":
        #        pLocation, iNumMoves, iScore = sVar1, iVar1, iVar2
        #That's all we have for now
        
            
        if sInput == "north":
            pPlayer.pLocation = SetLocation(pPlayer, 0) #0 = North

        elif sInput == "south":
            pPlayer.pLocation = SetLocation(pPlayer, 1) #1 = South

        elif sInput == "east":
            pPlayer.pLocation = SetLocation(pPlayer, 2) #2 = East

        elif sInput == "west":
            pPlayer.pLocation = SetLocation(pPlayer, 3) #3 = West
        
        elif(sInput == "help"):
            print("List of commands:\n"
                  "North: moves player in the 'north' direction.\n"
                  "South: moves player in the 'south' direction.\n"
                  "East: moves player in the 'east' direction.\n"
                  "West: moves player in the 'west' direction.\n"
                  "Help: displays a list of commands.\n"
                  "Quit: ends the game. Considered a game over.\n" #AKA run the game over/copyright function on quit
                  "Map: Displays the current map.\n"
                  "Moves: Shows how many moves you've made on this map.\n"
                  "Score: Displays your score.\n"
                  "Look: Displays the long description of the current location\n"
                  "Examine: Searches the location. Will reveal any item, if there is one.\n"
                  "Take: Take any item found at location with examine.")

        elif(sInput == "quit"):
            sInput = input("This will end the game and count as a game over. Continue?\n" #Changing sInput shouldn't cause issues
                           "<Enter 'y' for 'yes or 'n' for no'>\n")
            sInput = sInput[0].lower()

            if(sInput == "y"):
                Copyright(pPlayer, True)

        elif(sInput == "map"):
            i = GetLocation(pLocation)
            #Does the player HAVE a map?
            if DoesHaveItem(pMap, tPlayerInventory) or i < 6:
            
                if i > 5 and i < 27: #Always plan for the future... not that I have anything planned
                    print(gMap)
                    print(gMapDesc)
                    print("You are at:", tMap[i])
                else:
                    print(gMapTut)
            else:
                print("Map?")
                
        elif sInput == "moves":
             print("Your moves:", pPlayer.iMoves)

        elif sInput == "score":
             print("Your score:", pPlayer.iScore)
             
        elif sInput == "examine":
            print(tLocationsExamine[pPlayer.pLocation.i])
            
            if not DoesHaveItem(tLocationsItem[i], tPlayerInventory): 
                tCanPickup[i] = True
                
        elif sInput == "look":
            print(pPlayer.pLocation.sDescLong)

        elif sInput == "take":
           tPlayerInventory = Pickup(pPlayer) 
            
        else:
            print("Command not valid")
        ##LOCATION MUTATORS
        #Did the player enter the center of the office?
        #if pPlayer.pLocation.sDescShort == pOfficeC.sDescShort:
        #    SwitchLocations(iOfficeW, 3, iOfficeE, 2)
        #Did the player go to the lake?
        #elif pLocation == tLocationsLong[iLake] or pLocation == tLocationsShort[iLake]:
        #    #Unblock Cave
        #    ReplaceLocation(iWaterfall, 2, iCaveEnt)

        #Did the player go to the waterfall before going to the lake?
        #elif pLocation == tLocationsLong[iWaterfall] or pLocation == tLocationsShort[iWaterfall]:
        #    if tVisited[iLake] == False:
                #Block the lake
        #        ReplaceLocation(iRiver, 3, iWaterfallTop)
        #Did the player go the Forest?
        #elif pLocation == tLocationsLong[iForest] or pLocation == tLocationsShort[iForest]:
            #Is the Lake blocked?
        #    if mLocations[iRiver][3] == iWaterfallTop:
                #Unblock the Lake
        #        ReplaceLocation(iRiver, 3, iLake)
            
        ##ENDINGS
        #End of tutorial
        #if GetLocation(pLocation) < 6 and tVisited[iVoidM] and tVisited[iVoidN] and tVisited[iVoidS] and tVisited[iVoidE] and tVisited[iVoidW]:
        #    bGameState = False
        #    print(pLocation)
        #Reaching move limit
        #elif iNumMoves > 30 and GetLocation(pLocation) > 5 and bDoShowSequence:
        #    print(pLocation)
        #    print("\nBaby: Well, you certainly seem to be underperforming. It's quite boring actually. "
        #          "SERIOUSLY, what could be taking you so long?")
        #    #If the player is missing this item, end the game
        #    if not DoesHaveItem(pIdol, tPlayerInventory):
        #        bGameState = False
        #        print("Baby: Whatever. Nap time!")
                
        #    else:
        #        print("Baby: Mm. You're close, I'll give you that. Don't. Waste. My. Time.")
        #        bDoShowSequence = False
        #Cave Ending
        #elif pLocation == tLocationsLong[iCaveDeep] or pLocation == tLocationsShort[iCaveDeep]:
        #   bGameState = False
        #   print(pLocation)
           
        #   if DoesHaveItem(pIdol, tPlayerInventory):
        #      print("\nBaby: Welcome! Aw, look at that, you brought a gift. How thoughtful.")
        #      print("Baby: Anyways, let's stop for now. Got a clue as for where you are? Here's a hint: "
        #            "you're not in the real world! You're a smart being; you already knew that, right? Love love!")
        #      print("Final Score:", iScore)
        #      Copyright(iScore, False) #It is the end game but not a game over
        #      print("Thanks for playing!")
        #      sys.exit()
              
        #   else:
        #      bGameState = False
        #      print("\nBaby: Welcome!")
        #      print("Baby: To the great Greek god Zeus, a second is a thousand years. Now give me a second to congratulate you.")
              #sleep(1000) #I'm not that cruel 
        #My favorite ending
        #elif pLocation == tLocationsShort[iCloset] and iNumMoves > 0:
        #    bGameState = False
        #    print(pLocation)
        #    print("Suddenly the door slams shut behind you. You go to open it, only for the handle to fall off.")
        #    print("Baby: Eh, did you get the Broom Closet Ending? The Broom Closet Ending is my favourite!") #I spelt favourite like that intentionally by the by
        #Fell down the Ravine ending
        #elif pLocation == tLocationsLong[iRavine]:
        #    bGameState = False
        #    print(pLocation)
        #    print("\nBaby: Oops, looks like someone found their mortality!")           
        

Init()
    

