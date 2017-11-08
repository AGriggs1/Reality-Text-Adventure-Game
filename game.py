# Intro to Programming
# Author: Anthony Griggs
# Date: 9/12/17

#Project4
#Ver 0.7 11/8/17

from time import sleep # :) Only once
import sys #Learned about this from https://stackoverflow.com/questions/949504/terminating-a-python-program
          
cont = "<Press enter to "
bDevMode = True
#These have to defined before the nav matrix now
iVoidStart = 0
iVoidM = 1
iVoidN = 2
iVoidS = 3
iVoidE = 4
iVoidW = 5

iCloset = 6
iHallway1 = 7
iOfficeNW = 8
iOfficeW = 9
iOfficeSW = 10
iOfficeN = 11
iOfficeC = 12
iOfficeS = 13
iOfficeNE = 14
iOfficeE = 15
iOfficeSE = 16
iHallway2 = 17
iForest = 18
iRiver = 19
iLake = 20
iWaterfall = 21
iCaveEnt = 22
iCave = 23
iCaveDeep = 24
iRavine = 25
#Navigation Matrix
#This SHOULD be mutable'
#I just need to devise a way to mutate it
mLocations = [
            #c0-3 = N, S, E, W
            ##===FIRST MAP=========##
            [None, None, None, None],   #-------------r0 - VoidM (Intro)
            [iVoidN, iVoidS, iVoidE, iVoidS], #-----------r1 - VoidM
            [None, iVoidM, None, None], #--------------r2 - VoidN
            [iVoidM, None, None, None], #--------------r3 - VoidS
            [None, None, iVoidM, None], #--------------r4 - VoidE
            [None, None, None, iVoidM], #--------------r5 - VoidW
            ##===SECOND MAP========##
            [iHallway1, None, None, None], #---------------r6 -- Closet
            [None, iCloset, iOfficeW, None], #-------------r7 -- Hallway1
            [None, iOfficeW, iOfficeN, None], #------------r8 -- OfficeNW
            [iOfficeNW, iOfficeSW, iOfficeC, iHallway1], #-r9 -- OfficeW
            [iOfficeW, None, iOfficeS, None], #------------r10 - OfficeSW
            [None, iOfficeC, None, iOfficeNW], #-----------r11 - OfficeN
            [iOfficeN, iOfficeS, iOfficeE, iOfficeW], #----r12 - OfficeC
            [iOfficeC, None, iOfficeSE, iOfficeSW], #------r13 - OfficeS
            [None, iOfficeE, None, None], #----------------r14 - OfficeNE
            [iOfficeNE, iOfficeSE, iHallway2, iOfficeC], #-r15 - OfficeE
            [iOfficeE, None, None, iOfficeS], #------------r16 - OfficeSE
            [None, iForest, None, iOfficeE], #-------------r17 - Hallway2
            [None, iRiver, None, None], #------------------r18 - Forest
            [iForest, None, iWaterfall, iLake], #----------r19 - River
            [None, None, iRiver, None], #------------------r20 - Lake
            [None, None, iCaveEnt, iRiver], #--------------r21 - Waterfall
            [None, iCave, None, iWaterfall], #-------------r22 - CaveEnt
            [iCaveEnt, iRavine, None, iCaveDeep], #--------r23 - Cave
            [None, None, None, None], #---------------------r24 - CaveDeep
            [None, None, None, None] #---------------------r25 - Ravine(Hidden location, does not appear on map. Eventually the entire cave system won't appear on the map)

            ]
    
#Table of locations (long description) Displayed on first entry to location, or with 'look'           
tLocationsLong = [  
                #0 - VoidM (Intro)
                "You awake to find yourself in an empty white space.",
                #1 - VoidM
                "You are in an empty white space. A red circle with four lines leading in four directions to four other circles appears under your feet.", 
                #2 - VoidN
                "You follow one of the lines to a circle that, upon investigation, has the letter 'N' on it."
                "The area around you transforms into a forest filled teeming monstrous redwood trees. You hear the songs of various birds, and feel welcome.", 
                #3 - VoidS
                "You follow one of the lines to a circle that, upon investigation, has the letter 'S' on it. The area around you transforms." 
                "Suddenly you are at the edge of a cliff overlooking the open sea. You hear the waves crashing against the crags below you, "
                "smell the mist of saltwater, and feel a sense of somberness.",
                #4 - VoidE
                "You follow one of the lines to a circle that, upon investigation, has the letter 'E' on it. The area around you transforms and you are on the streets of a city that seems to be long abandoned. "
                "Cars rusted, buildings crumbling, overgrown with moss and vines. You can't help but feel curious about the fate of this place.",
                #5 - VoidW
                "You follow one of the lines to a circle that, upon investigation, has the letter 'W' on it. The area around you transforms into an office."
                "Desks teeming with paperwork and the faint smell of morning coffees makes you anxious.",
                #6 - Closet
                "You are in a broom closet. The shelves are littered with various objects. Perhaps there is something of use?",
                #7 - Hallway
                "You walk down a hallway and come to a corner.",
                #8 - OfficeNW
                "You enter one of the office corners. Papers and supplies litter the floor.", 
                #9 - OfficeW
                "You come to a large room full of cubicles, cubicles, cubicles. The building you're in must be an office, then.",
                #10 - OfficeSW
                "You enter one of the office corners, which has a particuliarly large ficus. You study it with intensity.",
                #11 - OfficeN
                "You enter a cubicle that is larger than all the rest. It looks like it's supposed to fit 4, maybe 5 people. The thought makes you feel claustrophobic.",
                #12 - OfficeC
                "You enter the center of the office.",
                #13 - OfficeS
                "You find a pair of doors. What lies beyond them?",
                #14 - OfficeNE
                "You enter on the office corners. There is a water cooler, but's its empty.",
                #15 - OfficeE
                "You are now on the other side of the office. Something feels off, or perhaps you just sick of this place.", #I wonder why
                #16 - OfficeSE
                "You enter one of the office corners. There is a painting of a sad clown. What?",
                #17 - Hallway
                "You walk down a hallway, and come to a corner.", #We need all the strings to be different for GetLocation to be precise
                #18 - Forest
                "You open the door and you suddenly find yourself in a forest. You look behind to find all traces of the office building to be gone."
                " All you see are trees, but you can hear the sound of running water.",
                #19 - River
                "You come to a river bank. You faintly hear what sounds like constant thunder.",
                #20 - Lake
                "You follow the river to a large lake.",
                #21 - Waterfall
                "You follow the river to a waterfall. It looks like it's about 15 feet height, but what do you know?",
                #22 - CaveEntrance
                "Behind the waterfall you find an entrance to a cavern. What lies within?",
                #23 - Cave
                "You go down into cave. It's pitch black, and you walk slowly and with caution.",
                #24 - DeepCave, End
                "You go deeper into the cave. You come to an empty chamber with a small opening to the surface, allowing you to see.",
                #25 - Ravine, End
                "You take a step forward, not knowing there is nowhere to place your foot. Suddenly, you find yourself tumbling down, down, down..."
                " You hit the bottom of the ravine. Hard. You cannot see how broken you are, but you know it's bad. You begin to lose consciousness."
                ]
bHasLight = True #I know globals are no-nos, but I NEED
sRavine = "With your source of light, you see a large drop-off to the south side. You can't see the bottom from here." #I'm not sure you can use other parts of a list when defining a list.
#Table of short location descriptions. Displayed after the location has been visited by default
tLocationsShort = [
                #0 - Void (Intro)
                None,
                #1 - VoidM
                "You are in the center of the void.",
                #2 - VoidN
                "You return to the forest.",
                #3 - VoidS
                "You return to the cliffside.",
                #4 - VoidE
                "You return to the city ruins.",
                #5 - VoidW
                "You return to the office.",
                #6 - Closet
                "You are in a broom closet.",
                #7 - Hallway
                "You are at a hallway corner.",
                #8 - OfficeNW
                "You enter the Northwest corner of the office.",
                #9 - OfficeW
                "You are in the office.",
                #10 - OfficeSW
                "You enter the Southwest corner of the office.",
                #11 - OfficeN
                "You are in the large cubicle.",
                #12 - OfficeC
                "You are in the center of the office.",
                #13 - OfficeS
                "You head towards the double doors.",
                #14 - OfficeNE
                "You are in the Northeast corner of the office.",
                #15 - OfficeE
                "You are in the office. ", #The space should make it unique...
                #16 - OfficeSE
                "You're in the Southeast corner of the office.",
                #17 - Hallway
                "You are at a hallway corner. ",
                #18 - Forest
                "You are in the forest. ",
                #19 - River
                "You are at the river.",
                #20 - Lake
                "You return to the lake.",
                #21 - Waterfall
                "The waterfall stands before you. Lovely.",
                #22 - Cave Entrance
                "You are behind the waterfall, at the maw of a cavern.",
                #23 - Cave
                "You are within the Cavern. ", #+ bHasLight and sRavine or None, #(<Boolean> AND <String> OR None) chooses <String> at True, None at False :( Python ain't havin it
    
                #24 - Deep Cave
                None, #I'M LAZY
                #25 - Ravine
                "With your source of light, you see a large drop-off to the south side. You can't see the bottom from here."
                ]
#Define table that holds booleans for whether or not the player has visited certain locations
tVisited = []
#For each location, append a False boolean to start with
for i in tLocationsShort:
    tVisited.append(False)

##=============================================================    
def Init(): #Initialization function, runs when the code is run
            #Basically, it's the introduction, and in hinesight it's really, really long, now that I think about it.
            #Hm, I'll see about cuttting it down, or making it skippable, since the first game loop is only there as a tutorial
            #I actually had a second run through main planned. That's why its def calls for a boolean called 'bFirstRun'
            #Thank me
##=============================================================
    tLocScore = [] #Let's just define this here
    iScore = 0
    sTitle = ( "*********   *********      ***      *           *********   *********   *       *\n" 
               "*       **  *              * *      *               *           *        *     *\n"
               "*        *  *             ** **     *               *           *         *   *\n"
               "*       **  *             *   *     *               *           *          * *\n"
               "*********   *********    *******    *               *           *           *\n"
               "*       **  *            *     *    *               *           *           *\n"      
               "*        *  *           **     **   *               *           *           *\n"           
               "*        *  *********   *       *   *********   *********       *           *\n")           #Dios ayudame si yo decido hacer un titulo nuevo.
    print(sTitle)
    tVisited[iVoidStart] = True
    tVisited[iVoidM] = True #They're technically the same
    pLocation, iNumMoves, iScore = SetLocation("None", iVoidStart, 0, 0)
    
    #Begin introduction
    print(pLocation)      
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
        print("Suddenly a red circle appears beneath your feet. You notice four lines spreading outward from it in four directions, leading to other circles\n")
        print("???: Okie-dokie, go ahead and walk towards any of these circles. I know you're confused, but stick with me. If you feel you need help, just say the word.\n")
        print("<Type 'North', 'South', 'East', or 'West' to head in that direction. To see all commands availible to you, type 'Help'>\n")
    
        #Update pLocation to showcase changes made
        pLocation, iNumMoves, iScore = SetLocation("None", iVoidM, 0, 0)
        #Enter the gamestate for the first time
        #SO I REMEMBER: in tLocScore, first index is location, second is score
        pLocation, iScore = Main(pLocation, sName, iScore, 0, True) #We need to send pLocation back to init(), don't we? I'll have to think about implementing that #SOLVED leaving so you can probe my thought process
        #Begin second half of in intro
        print("\n???: Excellent, " + sName + ". You seem to be in optimal shape. Excellent indeed.\n"
              "You're patience with me has not gone unnoticed. I... do not have not been aquainted. I am Bx106001-c. I am a Generation IV Class C Artificial Intelligence. You may call me Baby.\n"
              "Baby: I know you are curious as for where you are, but that's a bit more difficult. Could you define what exactly you wish to know about your whereabouts?\n")
    
        input() #Hm, is Baby decieving you?
        print("Baby: ERROR: Acess denied.")
        sleep(1)
    
        for i in range(150):
            print("x003334" + str(i) + ".FATAL: Bx106001-c Gen IV 'Bravo-Alfa-Bravo-Yankee' has @#4uNt2#d an is$3@ that has co#$Afg0sed *&ad$%3-sufficient operations!") #Baby has ecountered an issue that has compromised self-sufficient operations!
        #for i in range(20):
           # print()
        print("Baby: Oops! Looks I had a little hiccup there.\n"
              "Baby: I'm sorry, but you don't have permission to access such information without the correct access code. Please input access code now.")
        #Hmmm, maybe I could add a little easter egg here
        input("Access code: ")
    
        print("Baby: Nuh-uh. Wrong, as expected. Hm, tell you what, I'll at least tell you what you're here for. This place, whatever it may be to you, is to test your physical and cognitive abilities.\n"
              "Baby: I... am to test you. You pass this, and Baby will tell you anything.\n"
              "I may even let you go free!\n"
              "...") #In the future, 'Baby:' should be a var
    
        input(cont + "question Baby>")
        print("Baby: This test is not optional! You're going to participate and you're going to love it! You'll see...\n"
              "Baby: Let's start!")
    pLocation = tLocations[iCloset]
    pLocation, iScore = Main(pLocation, sName, iScore, 0, False)
    Copyright(iScore, True)
    
    
    
    #return sName #Send to global variable. #NEVER GETS USED
##==============================================
#SetLocation
#Sets the player's location
#Parameters:
    #sLocation, the player's current location
    #iTo, the index of the location the player is moving to
    #iMoves, the number of moves
##==============================================
def SetLocation(sLocation, iTo, iNumMoves, iScore):
    sLocation = tLocations[iTo]

    if not tVisited[iTo]:
        iScore = iScore + 5
        tVisited[iTo] = True
    iNumMoves = iNumMoves + 1
    return sLocation, iNumMoves, iScore

def GetLocation(sLocation):
    
    for i in range(len(tLocations) - 1):
        
        if tLocations[i] == sLocation:
            return i
    print("Error: pLocation not found")
    return None
##================================
#Copyright
#Prints the copyright/gameover statement
#Parameters:
    #iScore, the player's score
    #bGameover, used to determine if the gameover statement should be printed
##================================
def Copyright(iScore, bGameover):
    sMessage = "Copyright Anthony Griggs. Email inquiries to Anthony.Griggs1@marist.edu"

    if bGameover:
        print("Final score:", iScore)
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
            sInput = input("???: Hey, hey, what do you think you're doing trying to skip my glorius introduction, bub? Do you even know my name? ")

            if sInput.lower() == "baby":

                print("Baby: ...")
                sInput = input("Baby: Fine! What's you're name, dum-dum?")
                return False, sInput  #May change the return values in the future
            else:
                print("???: Hmph! Hm hm! HM HM HM HM! Let's reimmerse ourselves, yeah? *Ahem*")
                return True, "It's Baby"
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


##===========================================
#Main
#Gamestate function, always active while player is in the game
#Parameters:
#   *sLocation, the location to start the game at
#   *sName, the name the player chose
#   *iScore, the player's score at this point of the game
#   *bFirstRun, indicate whether or not this is the first instance of firing the loop (In other words, is the intro still on-going?)
##============================================
sNoGo = "You can't go that way."
gMapTut = ("   N    \n"
           "   |    \n"
           "W--M--S \n"
           "   |    \n"
           "   S    \n")

gMap = ("   c1--C   c6            \n"
        "   |   |   |             \n"
        "b--c2--c4--c7--d         \n"
        "|  |   |   |   |         \n"
        "a  c3--c5--c8  e         \n"
        "               |         \n"
        "            g--f--h--i   \n"
        "                     |   \n"
        "                  k--j   \n")

gMapDesc = ("a = Closet\n"
            "b = Hallway Corner\n"
            "Cc = Office\n"
            "d = Other Hallway Corner\n"
            "e = Forest\n"
            "f = River\n"
            "g = Lake\n"
            "h = Waterfall\n"
            "i = Cave\n"
            "j = Deep Cave\n"
            "k = ???")
tMap = ["Error: Could not determine location", "M", "N", "S", "E", "W", "a", "b", "c1", "c2", "c3", "C", "c4", "c5", "c6", "c7", "c8", "d", "e", "f", "g", "h", "i", "j", "k"]
#Since the location at 0 is not used in the game loop, it can be used to display an error message
#But for now we'll stick with the is not None check

def Main(sLocation, sName, iScore, iNumMoves, bFirstRun):
    pLocation = sLocation
    bGameState = True

    
    while bGameState:
        print(pLocation)
        sInput = input()
        sInput = sInput.lower()
        bVar1, sVar1, sVar2, iVar1, iVar2, sResult = Interpret(sInput, pLocation, iScore, iNumMoves, "Main")#This is going to get hideous
        #Now we just need to interpret the return values here by looking at sResult
        #if sResult is not none:
        #   if sResult is "setlocation":
        #        pLocation, iNumMoves, iScore = sVar1, iVar1, iVar2
        #That's all we have for now
        
        if bFirstRun:
            if sInput == "north":
            
                if pLocation == tLocations[iVoidM]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iVoidN, iNumMoves, iScore)

                elif pLocation == tLocations[iVoidS]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iVoidM, iNumMoves, iScore)
            
                else:
                    #Can't go that way
                    print(sNoGo)

            elif sInput == "south":

                if pLocation == tLocations[iVoidM]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iVoidS, iNumMoves, iScore)

                elif pLocation == tLocations[iVoidN]:
                     pLocation, iNumMoves, iScore = SetLocation(pLocation, iVoidM, iNumMoves, iScore)

                else:
                    print(sNoGo)

            elif sInput == "east":

                if pLocation == tLocations[iVoidM]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iVoidE, iNumMoves, iScore)

                elif pLocation == tLocations[iVoidW]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iVoidM, iNumMoves, iScore)

                else:
                   print(sNoGo)
            elif sInput == "west":

                if pLocation == tLocations[iVoidM]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iVoidW, iNumMoves, iScore)

                elif pLocation == tLocations[iVoidE]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iVoidM, iNumMoves, iScore)
                else:
                    print(sNoGo)
        elif not bFirstRun:
            if sInput == "north":

                if pLocation == tLocations[iCloset]:
                     pLocation, iNumMoves, iScore = SetLocation(pLocation, iHallway1, iNumMoves, iScore)

                elif pLocation == tLocations[iOfficeSW]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iOfficeW, iNumMoves, iScore)

                elif pLocation == tLocations[iOfficeS]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iOfficeC, iNumMoves, iScore)

                elif pLocation == tLocations[iOfficeSE]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iOfficeE, iNumMoves, iScore)

                elif pLocation == tLocations[iOfficeW]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iOfficeNW, iNumMoves, iScore)

                elif pLocation == tLocations[iOfficeC]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iOfficeN, iNumMoves, iScore)

                elif pLocation == tLocations[iOfficeE]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iOfficeNE, iNumMoves, iScore)
                #You can't go back to the office from the forest
                elif pLocation == tLocations[iRiver]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iForest, iNumMoves, iScore)

                elif pLocation == tLocations[iCave]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iCaveEnt, iNumMoves, iScore)
                
                else:
                    print(sNoGo)
            elif sInput == "south":

                if pLocation == tLocations[iHallway1]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iCloset, iNumMoves, iScore)

                elif pLocation == tLocations[iOfficeNW]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iOfficeW, iNumMoves, iScore)

                elif pLocation == tLocations[iOfficeN]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iOfficeC, iNumMoves, iScore)

                elif pLocation == tLocations[iOfficeNE]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iOfficeE, iNumMoves, iScore)

                elif pLocation == tLocations[iOfficeW]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iOfficeSW, iNumMoves, iScore)

                elif pLocation == tLocations[iOfficeC]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iOfficeS, iNumMoves, iScore)

                elif pLocation == tLocations[iOfficeE]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iOfficeSE, iNumMoves, iScore)

                elif pLocation == tLocations[iHallway2]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iForest, iNumMoves, iScore)

                elif pLocation == tLocations[iForest]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iRiver, iNumMoves, iScore)

                elif pLocation == tLocations[iCaveEnt]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iCave, iNumMoves, iScore)

                else:
                    print(sNoGo)
            elif sInput == "east":

                if pLocation == tLocations[iHallway1]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iOfficeW, iNumMoves, iScore)

                elif pLocation == tLocations[iOfficeNW]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iOfficeN, iNumMoves, iScore)

                #elif pLocation == tLocations[iOfficeN]:
                #    pLocation, iNumMoves, iScore = SetLocation(pLocation, iOfficeNE, iNumMoves, iScore)

                elif pLocation == tLocations[iOfficeW]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iOfficeC, iNumMoves, iScore)

                elif pLocation == tLocations[iOfficeC]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iOfficeE, iNumMoves, iScore)

                elif pLocation == tLocations[iOfficeE]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iHallway2, iNumMoves, iScore)

                elif pLocation == tLocations[iOfficeSW]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iOfficeS, iNumMoves, iScore)

                elif pLocation == tLocations[iOfficeS]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iOfficeSE, iNumMoves, iScore)

                elif pLocation == tLocations[iLake]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iRiver, iNumMoves, iScore)

                elif pLocation == tLocations[iRiver]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iWaterfall, iNumMoves, iScore)

                elif pLocation == tLocations[iWaterfall]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iCaveEnt, iNumMoves, iScore)

                else:
                    print(sNoGo)

            elif sInput == "west":

                if pLocation == tLocations[iOfficeW]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iHallway1, iNumMoves, iScore)

                elif pLocation == tLocations[iOfficeN]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iOfficeNW, iNumMoves, iScore)

                #elif pLocation == tLocations[iOfficeNE]:
                #    pLocation, iNumMoves, iScore = SetLocation(pLocation, iOfficeN, iNumMoves, iScore)

                elif pLocation == tLocations[iOfficeC]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iOfficeW, iNumMoves, iScore)

                elif pLocation == tLocations[iOfficeE]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iOfficeC, iNumMoves, iScore)

                elif pLocation == tLocations[iHallway2]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iOfficeE, iNumMoves, iScore)

                elif pLocation == tLocations[iOfficeS]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iOfficeSW, iNumMoves, iScore)

                elif pLocation == tLocations[iOfficeSE]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iOfficeS, iNumMoves, iScore)

                elif pLocation == tLocations[iRiver]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iLake, iNumMoves, iScore)

                elif pLocation == tLocations[iWaterfall]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iRiver, iNumMoves, iScore)

                elif pLocation == tLocations[iCaveEnt]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iWaterFall, iNumMoves, iScore)

                elif pLocation == tLocations[iCave]:
                    pLocation, iNumMoves, iScore = SetLocation(pLocation, iCaveDeep, iNumMoves, iScore)
                    
                else:
                    print(sNoGo)
        if sInput == "north" or sInput == "south" or sInput == "west" or sInput == "east":
            pass #We already checked for these, now we just need them here to verify if the player entered a valid command or not
        
        elif(sInput == "help"):
            print("List of commands:\n"
                  "North: moves player in the 'north' direction.\n"
                  "South: moves player in the 'south' direction.\n"
                  "East: moves player in the 'east' direction.\n"
                  "West: moves player in the 'west' direction.\n"
                  "Help: displays a list of commands. Hey, a dictionary's gotta have the definition of a dicitionary in it.\n"
                  "Quit: ends the game. Considered a game over.\n" #AKA run the game over/copyright function on quit
                  "Map: Displays the current map.\n"
                  "Moves: Shows how many moves you've made on this map.\n"
                  "Score: Displays your score.")

        elif(sInput == "quit"):
            sInput = input("This will end the game and count as a game over. Continue?\n" #Changing sInput shouldn't cause issues
                    "<Enter 'y' for 'yes or 'n' for no'>\n")
            sInput = sInput[0].lower()

            if(sInput == "y"):
                Copyright(iScore, True)

        elif(sInput == "map"):

            if bFirstRun:
                print(gMapTut)
                index = GetLocation(pLocation)

                if index is not None:
                    print("\nYou are at:", tMap[index])
                          
            else:
                print(gMap)
                print(gMapDesc)
                index = GetLocation(pLocation)

                if index is not None:
                    print("\nYou are at:", tMap[index])

        elif sInput == "moves":
             print("Your moves:", iNumMoves)

        elif sInput == "score":
             print("Your score:", iScore)

        else:
            print("Command not valid")

        if bFirstRun and tVisited[iVoidM] and tVisited[iVoidN] and tVisited[iVoidS] and tVisited[iVoidE] and tVisited[iVoidW]:
            bGameState = False
            print(pLocation)

        elif iNumMoves > 30 and not bFirstRun:
            bGameState = False
            print(pLocation)
            print("\nBaby: Well, you certainly seem to be underperforming. It's quite boring actually. Looks like it's back to stasis for you!")
            #Activate bad end

        elif pLocation == tLocations[iCaveDeep]:
            bGameState = False
            print(pLocation)
            print("\nBaby: Good. Hmmm, listen, I've got to deal with something, why don't you take a rest, and then we can talk. Probably. See you in 50 years!")
            #Activate less bad end
    tLocScore = []
    tLocScore.append(pLocation)
    tLocScore.append(iScore)
    return pLocation, iScore
        

Init()
    

