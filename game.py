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
#Here. Now.
bDevMode = True


pDoll = "Doll"
pMapOffice = "Map"
pMapOther = "Map"
pMap = "Map" #You can combine items to create a new one
pFlashlight = "Flashlight"
pBatteries = "Batteries"
pHammer = "Hammer"
pRope = "Rope"
pBlockN = "N-block"
pBlockS = "S-block"
pBlockE = "E-block"
pBlockW = "W-block"
pMatches = "Matches"
pKey = "Key"
#Define area specific maps
gMapOffice = ("   c1--C   c6     \n"
              "   |   |   |      \n"
              "b--c2--c4--c7--d  \n"
              "|  |   |   |   |  \n"
              "a  c3--c5--c8  e  \n"
              "       |          \n"
              "       |          \n"
              "   51--n1--40     \n"
              "     - |  +      \n"
              "   50--n2--48     \n"
              "     + |  -      \n"
              "   45--n3--42     \n"
              "     = |  =      \n"
              "     = 46 =        ")
              #This is how the corridor is supposed to be. It's not, of course, but this is how you tell

gMapForest = ("   e          \n"
              "   |          \n"
              "g--f--h--i    \n"
              "         |    \n"
              "      j--k    \n"
              "         |    \n"
              "         l--m   ")
#This matrix defines the indexes of the locations each item can be used at
#It will be used like this:
# for i in mCanUseAt[row]:
#   if i == pLocation.i:
#etcetera
mCanUseAt = [
    [], #r0 - Doll
    [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27], #r1 - Map Office, Map Other, Map
    [23], #r2 - Flashlight
    [], #r3 - Batteries
    [7, 28], #r4 - Hammer
    [23], #r5 - Rope
    [], #r6 - N-Block
    [], #r7 - S-Block
    [],  #r8 - E-Block
    [], #r9 - W-Block
    [24], #r10 - Matches
    [13], #r11 - Key
    ]
#Defines if items can be used
#Useful for items that need other items first
#or one use items
tCanUse = [True, #r0 - Doll
           True, #r1 - Maps
           False, #r2 - Flashlight
           True, #r3 - Batteries
           True, #r4 - Hammer
           False, #r5 - Rope
           False, #r6 - N-Block
           False, #r7 - S-Block
           False, #r8 - E-Block
           False, #r9 - W-Block
           True, #r10 - Matches
           True, #r11 - Key
           ]
           
pVoidDummy = Locale("You find yourself in an empty white space, a 'nothing'.", None, 0, [])
pVoid = Locale("You are in an empty white space. A red circle with four lines leading in four directions"
               " to four other circles appears under your feet.",
               "You are in the center of the void.", 1, [pBlockS, pBlockW]) #For now, I just want to define every location, so I'll just list the name of the item.

pVoidN = Locale("You follow one of the lines to a circle that, upon investigation, has the letter 'N' on it."
                "The area around you transforms into a forest filled teeming monstrous redwood trees."
                "You hear the songs of various birds, and feel welcome.",
                "You return to the forest", 2, [pBlockE])

pVoidS = Locale("You follow one of the lines to a circle that, upon investigation, has the letter 'S' on it."
                "The area around you transforms. Suddenly you are at the edge of a cliff overlooking the open sea."
                "You hear the waves crashing against the crags below you, smell the mist of saltwater, and feel a sense of somberness.",
                "You return to the cliffside", 3, [pBlockN])

pVoidE = Locale("You follow one of the lines to a circle that, upon investigation, has the letter"
                "'E' on it. The area around you transforms and you are on the streets of a city that seems to be long abandoned. "
                "Cars rusted, buildings crumbling, overgrown with moss and vines. You can't help but feel curious about the fate of this place.",
                "You return to the city ruins", 4, [])

pVoidW = Locale("You follow one of the lines to a circle that, upon investigation, has the letter 'W' on it. "
                "The area around you transforms into an office."
                "Desks teeming with paperwork and the faint smell of morning coffees makes you anxious.",
                "You return to the office", 5, [])

pCloset = Locale("You are in a broom closet. The shelves are littered with various objects. Perhaps there is something of use?",
                 "You're in a broom closet.", 6, [pFlashlight, pMatches, pHammer])

pHallway1 = Locale("You walk down a hallway and come to a corner.",
                   "You are at a hallway corner. ", 7, [pMapOffice])

pOfficeNW = Locale("You enter one of the office corners. Papers and supplies litter the floor.",
                   "You enter the Northwest corner of the office.", 8, [])

pOfficeW = Locale("You come to a large room full of cubicles, cubicles, cubicles. The building you're in must be an office, then.",
                  "You are in the office.", 9, [])

pOfficeSW = Locale("You enter one of the office corners, which has a particuliarly large ficus. You study it with intensity.",
                   "You enter the Southwest corner of the office.", 10, [pBatteries])
                   
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
                 "You are in the forest. ", 18, [pRope, pMapOther])

pRiver = Locale("You come to a river bank. You faintly hear what sounds like constant thunder.", "You are at the river.", 19, [])

pLake = Locale("You follow the river to a large lake. It's shores are sandy, interestingly enough.", "You return to the lake.", 20, [pDoll])



pWaterfall = Locale("You follow the river to a waterfall. It looks like it's about 15 feet high, but what do you know?", 
                "The waterfall stands before you. Lovely.", 21, [])

pCaveEnt = Locale("Behind the waterfall you find an entrance to a cavern. What lies within?",
                  "You are behind the waterfall, at the maw of a cavern.", 22, [])

pCave = Locale("You go down into cave. It's pitch black, and you walk slowly and with caution. ",
               "You are within the dark cavern. ", 23, [])

pCaveDeep = Locale("You go deeper into the cave. You come to an empty chamber with a small opening to the surface, allowing you to see."
                   " You take notice of the the many symbols drawn on the chamber floor in what could be chalk. Whatever it is, it looks"
                   " like it was for ritualistic purposes.",
                   "You are deep within the cave", 24, [])

pRavine = Locale( "You take a step forward, not knowing there is nowhere to place your foot. "
                "Suddenly, you find yourself tumbling down, down, down..."
                " You hit the bottom of the ravine. Hard. You cannot see how broken you are, but you know it's bad. "
                "You begin to lose consciousness.", "You are at the bottom of a ravine", 25, [])
                 
pWaterfallTop = Locale("Following the current, you come across the top of a waterfall. It looks like a 15-foot drop, but what do you know?",
                       "It's the top of a waterfall. Again.", 26, [])

pElevator = Locale("You make your way through the ravine, comming to... an elevator. Question is, up or down?",
                   "You are in the elevator", 27, [])

pElevatorUp = Locale("You push the 'up' button. You feel your weight shift as the box pushes you upward. The elevator stops at a 'ding!'"
                     ", the doors slide open to reveal... A wall. This doesn't seem right...", "You are in the elevator", 28, [])

pChairOffice = Locale("You walk down a large corridor to come to a large, furnished room. On the other side is a much is a large desk "
                      "and behind that desk is much, much larger portrait of Bobbo. Well then.", "You are in Bobbo's office", 29, [])

pCorridor1 = Locale("You open the double doors to reveal a long corrider. You are now standing at an intersection.",
                    "You are at one of the ends of the corridor, at an intersection.", 30, [])

pCorridor1E = Locale("You head east in the intersection. There is a door with a number on it.", "You are in the east end of the intersection.",
                    31, [])

pCorridor1W = Locale("You walk west in the intersection. There is a door with a number on it.", "You are in the west end of the intersection.",
                     32, [])
pCorridor2 = Locale("You head south down the corridor, stopping before the next intersection.", "You are in the long corridor.", 33, [])

pCorridor3 = Locale("You come to the next intersection.", "You are at an intersection.", 34, [])

pCorridor3E = Locale("You head east in the intersection. There is a door with a number on it.", "You are in the east end of the intersection.",
                     35, [])

pCorridor3W = Locale("You walk west in the intersection. There is a door with a number on it.", "You are in the west end of the intersection.",
                     36, [])

pCorridor4 = Locale("You continue south down the corridor, stopping before the next intersection.", "You are in the long corridor.", 37, [])

pCorridor5 = Locale("You enter the last intersection of the corridor.", "You are at the center of an intersection", 38, [])

pCorridor5E = Locale("You head east in the intersection. There is a door with a number on it.", "You are in the east end of the intersection",
                     39, [])

pCorridor5W = Locale("You walk west in the intersection. There is a door with a number on it.", "You are in the west end of the intersection",
                     40, [])

pCorridor6 = Locale("You walk south to the end of the corridor, There are a pair of doors, with the number '46' on them.", "You are before the 46 door.",
                    41, [])


tLocations = [pVoidDummy, pVoid, pVoidN, pVoidS, pVoidE, pVoidW,
                  pCloset, pHallway1, pOfficeNW, pOfficeW, pOfficeSW,
                  pOfficeN, pOfficeC, pOfficeS, pOfficeNE, pOfficeE,
                  pOfficeSW, pHallway2, pForest, pLake, pRiver,
                  pWaterfall, pCaveEnt, pCave, pCaveDeep, pRavine,
                  pWaterfallTop, pElevator, pElevatorUp, pChairOffice,
              pCorridor1, pCorridor1E, pCorridor1W, pCorridor2, pCorridor3, pCorridor3E,
              pCorridor3W, pCorridor4, pCorridor5, pCorridor5E, pCorridor5W, pCorridor6] #CAN'T BBOTHERED TO MOVE THIS OVER
#Navigation Matrix
mLocations = [
        #c0-5 = N, S, E, W, UP, DN
        ##===FIRST MAP=========##
        [None, None, None, None, None, None],   #-------------r0 - VoidM (Intro)
        [pVoidN, pVoidS, pVoidE, pVoidW, None, None], #-------r1 - VoidM
        [None, pVoid, None, None, None, None], #--------------r2 - VoidN
        [pVoid, None, None, None, None, None], #--------------r3 - VoidS
        [None, None, None, pVoid, None, None], #--------------r4 - VoidE
        [None, None, pVoid, None, None, None], #--------------r5 - VoidW
        ##===SECOND MAP========##
        [pHallway1, None, None, None, None, None], #---------------------r6 -- Closet
        [None, pCloset, pOfficeW, None, None, None], #-------------------r7 -- Hallway1
        [None, pOfficeW, pOfficeN, None, None, None], #------------------r8 -- OfficeNW
        [pOfficeNW, pOfficeSW, pOfficeC, pHallway1, None, None], #-------r9 -- OfficeW
        [pOfficeW, None, pOfficeS, None, None, None], #------------------r10 - OfficeSW
        [None, pOfficeC, None, pOfficeNW, None, None], #-----------------r11 - OfficeN
        [pOfficeN, pOfficeS, pOfficeE, pOfficeW, None, None], #----------r12 - OfficeC
        [pOfficeC, None, pOfficeSE, pOfficeSW, None, None], #------------r13 - OfficeS
        [None, pOfficeE, None, None, None, None], #----------------------r14 - OfficeNE
        [pOfficeNE, pOfficeSE, pHallway2, pOfficeC, None, None], #-------r15 - OfficeE
        [pOfficeE, None, None, pOfficeS, None, None], #------------------r16 - OfficeSE
        [None, pForest, None, pOfficeE, None, None], #-------------------r17 - Hallway2
        [None, pRiver, None, None, None, None], #------------------------r18 - Forest
        [pForest, None, pWaterfall, pLake, None, None], #----------------r19 - River
        [None, None, pRiver, None, None, None], #------------------------r20 - Lake
        [None, None, pCaveEnt, pRiver, None, None], #--------------------r21 - Waterfall
        [None, pCave, None,pWaterfall, None, None], #--------------------r22 - CaveEnt
        [pCaveEnt, pRavine, None, pCaveDeep, None, None], #--------------r23 - Cave
        [None, None, pCave, None, None, None], #-------------------------r24 - CaveDeep
        [pCave, None, None, None, None, None, None, None], #-------------r25 - Ravine
        [None, None, pRiver, pWaterfall, None, None], #------------------r26 - WaterfallTop(replaces lake)
        [None, None, None, None, pElevatorUp, None], #-------------------r27 - Elevator
        [None, None, None, None, None, pElevator], #---------------------r28 - ElevatorUp(Replace c1 with pOfficeSE)
        [None, None, None, None, None, None], #--------------------------r29 - Bobbo's Office (New end game)
        [pOfficeS, pCorridor2, pCorridor1E, pCorridor1W, None, None], #--r30 - Corridor1
        [None, None, None, pCorridor1, None, None], #--------------------r31 - Corridor1E
        [None, None, pCorridor1, None, None, None], #--------------------r32 - Corridor1W
        [pCorridor1, pCorridor3, None, None, None, None], #--------------r33 - Corridor2
        [pCorridor2, pCorridor4, pCorridor3E, pCorridor3W, None, None], #r34 - Corridor3
        [None, None, None, pCorridor3, None, None], #--------------------r35 - Corridor3E
        [None, None, pCorridor3, None, None, None], #--------------------r36 - Corridor3W
        [pCorridor3, pCorridor5, None, None, None, None], #--------------r37 - Corridor4
        [pCorridor4, pCorridor6, pCorridor5E, pCorridor5W, None, None], #r38 - Corridor5
        [None, None, None, pCorridor5, None, None], #--------------------r39 - Corridor5E
        [None, None, pCorridor5, None, None, None], #--------------------r40 - Corridor5W
        [pCorridor5, pForest, None, None, None] #------------------------r41 - Corridor6
        
            ]
sRavine = ("You take a step forward, not knowing there is nowhere to place your foot. "
                "Suddenly, you find yourself tumbling down, down, down..."
                " You hit the bottom of the ravine. Hard. You cannot see how broken you are, but you know it's bad. "
                "You begin to lose consciousness.")

#Define examine results
#Now, with DoExamine, this table will just be an in-depth description of findings
sNone = ""
tLocationsExamine = [           #Examine is dual purpose. It prints the index of this list based on location index and it checks if the location has an item
                #0 - None
                sNone,
                #1 - VoidM, None
                sNone,
                #2 - VoidN, None
                sNone,
                #3 - VoidS, None
                sNone,
                #4 - VoidE, None
                sNone,
                #5 - VoidW, None
                sNone,
                #6 - Closet, Map
                "You rifle through the shelves.",
                #7 - Hallway, None
                "There's a glass panel on the wall. Inside you see what could be a 'Map' of this place\n\n" + gMapOffice + "\nYou are at: a",
                #8 - OfficeNW, None
                "You rumage through the various papers and see nothing particuliarly interesting. Wait! Oh. Nevermind.",
                #9 - OfficeW, None
                sNone,
                #10 - OfficeSW, Flashlight
                "You look in the plant pot.",
                #11 - OfficeN, None
                "You try turning on one of the cubicle computers. It boots instantly to a text document that reads:\n"
                "\n'When the sun sets, the water shall chase it\n\nWhere they meet, among the sands, lies the key to"
                " the secret of their origin.'",
                #12 - OfficeC, None
                sNone,
                #13 - OfficeS, None
                "The doors simply won't budge. Is there a key somewhere? \n\nYou notice a panel next to the door: \n\n"
                "'Beyond this pair lies another... beyond it lies the office of the clown, but only when 46 and 46 is 46'", #Yes
                #14 - OfficeNE, None
                "Just an empty watercooler. What a shame.",
                #15 - OfficeE, None
                sNone,
                #16 - OfficeSE, None
                "The portrait has an inscription. It reads 'Chairman Bobbo the Clown, may he grace you with his gaze.' Yeah-huh.",
                #17 - Hallway, None
                "You don't see anything.", #Very subtle way to tell the difference between hallways
                #18 - Forest, Rope, ForestMap (In the future, this combined with the flashlight will let you safely explore the ravine
                "Nearby is a wooden bulletin board enscribed as 'New Pena National Forest'."
                " On it you see what looks like a map of the area:\n\n" + gMapForest + "\nYou are at: e\n"
                "On the board there is also a notice:\n\n"
                "'Explore one New Pena's many cave systems! See the ancient incantation circles where"
                " many a-locals performed rituals to please their deities! Book your guided tour now!\n"
                "WARNING: Cave spelunking can be a rigorous, high-demanding activity! DO NOT EXPLORE UNAUTHORIZED AREAS ALONE OR WITHOUT A GUIDE!'",
                #19 - River, None
                "Just a river here.",
                #20 - Lake, Idol
                "Along the lake shores you find a small wooden figureine, look some sort of 'Doll'.",
                #21 - Waterfall, None
                sNone,
                #22 - Cave Entrance, None
                sNone,
                #23 - Cave, None
                sNone,
                #24 - Deep Cave, None
                sNone,
                #25 - Ravine
                sNone,
                #26 - WaterfallTop
                sNone,
                #27 - Elevator
                sNone,
                #28 - ElevatorTop
                "Hold on... what's this in the center of the wall? It feels softer, like a canvas...",
                #29 - Chair Office
                sNone,
                #30 - Corridor1
                "The door at the end of this corridor... what might it lead to?",
                #31 - Corridor1E
                "The number on the door is 50. There is a red button by the door...",
                #32 - Corridor1W
                "The number on the door is 51. There is a green button by the door...",
                #33 - Corridor2
                "On the east side, there is a '+' painted on the wall. On the west side, there is a '-'.",
                #34 - Corridor3
                sNone,
                #35 - Corridor3E
                "The number on the door is 45. There is a blue button by the door...",
                #36 - Corridor3W
                "The number on the door is 42. There is a blue button by the door...",
                #37 - Corridor4
                "On the east side, there is a '-' painted on the wall. On the west side, there is a '+'.",
                #38 - Corridor5
                sNone,
                #39 - Corridor5E
                "The number on the door is 48. There is a red button by the door...",
                #40 - Corridor5W
                "The number on the door is  40. There is a green button by the door...",
                #41 - Corridor6
                "The double door has the number 46. On each side of the wall, there is an '=' sign with a number below that."
                ]



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
    #Reset locations

    for p in tLocations:
        p.ResetValues()
        #Based on the absolute bollocks of NOT being allowed to copy one variable to another without tieing the two together, we hafta do THIS
        #IF I want to something so trivially simple as reseting a data value to what it was when it was initialized
        #Allegedly. I have better things to test less tedious way
        s = p.DESC_LONG
        p.sDescLong = s
        s = p.DESC_SHORT
        p.sDescShort = s
    #Begin introduction
    print(pPlayer.pLocation.sDescLong) #Needs to be cleaned up, naturally    
    sInput = input("input: ") or "None"  #If sInput is None (player hits enter without typing anything) then fill it in with "None"

    
    sInput, pPlayer.sName = Interpret(sInput, pPlayer, "Init") #Hmmmm
    if sInput:
        print("???: Hey! Can you hear me?")
        input(cont + "continue>") #Must use concatenation for input
    
        print("???: Good. Now, I know you must have plenty of questions, such as where you are, or who I am. We'll get to them when the time comes.\n\n"
              "???: There are more pressing matters. Protocol insists that I perform a sitrep on your state of being before we can address any inquiries.\n"
              "Understand?")
    
        input(cont + "understand>")
        #Get player name
        pPlayer.sName = input("???: First things first: do you know your name?\nYour name? ")
    
        print("???: " + pPlayer.sName + "? All right. Now let's see about your sense of orientation.\n")
        print("Suddenly a red circle appears beneath your feet. You notice four lines spreading outward from it in four directions,"
              " leading to other circles\n")
        print("???: Now, There are 4 other circles in the 4 cardinal directions. What I want you to do is to 'examine' each area, 'take'"
              " any block with a letter enscribed on it you find and 'drop' them off where you think they belong. Got it?")
        
        print("<Type 'North', 'South', 'East', or 'West' to head in that direction, 'Examine' to look around the area for items, "
              "'Take' to take any found item and 'Drop' to put down that item. To see all commands availible to you, type 'Help'>\n")
    
        #Update pLocation to showcase changes made
        pPlayer.pLocation = pVoid
        #Enter the gamestate for the first time
        b = Main(pPlayer)
        if b: return b
        #Begin second half of intro
        print("\n???: Excellent, " + pPlayer.sName + ". You seem to be in optimal shape. Excellent indeed.\n"
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
        #This is changed here too for the boolean test below
        pPlayer.pLocation = pCloset
    #Block Cave
    ReplaceLocation(pWaterfall.i, 2, None)
   # pPlayer.pLocation = pCloset 
    #tVisited[iCloset] = True
    b = Main(pPlayer)
    if b: return b #The player quit
    b = Copyright(pPlayer, True)
    return b
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

##======================================
#Pickup
#Gives the player the item at sLocation
##======================================
def Pickup(pPlayer, pItem):
    pLocation = pPlayer.pLocation
    iItem = pLocation.GetItemIndex(pItem)

    if iItem is not None:

        #The item is at this location. Can it be picked up?
        #Hmm, do we want the boolean that determines if an item can
        #be picked up to be determined in the Locale class?
        #The tables indices need to stay in sync with each other
        if pLocation.tCanPickup[iItem]:

            pPlayer.tInventory.append(pItem)
            #Quick google search on lists
            #I didn't know pop can remove by index
            #I guess del is for general purpose deleting
            print(pLocation.ITEMS)
            print(pLocation.tCanPickup)
            #del(pLocation.tItems[iItem])
            #del(pLocation.tCanPickup[iItem])
            pLocation.tItems.pop(iItem)
            print(pLocation.tCanPickup)
            pLocation.tCanPickup.pop(iItem)
            print(pLocation.ITEMS)
            
            print("Picked up the", pItem + ".")
        else:
            if pItem == "Map":
                if pLocation == pHallway1:
                    print("The map is behind the glass. You can't get to it.")
    else:
        print("Could not find any", pItem, "here.")
##=======================
#Drop
#Drops the defined item the current location
##=======================
def Drop(pPlayer, pItem):
    pLocation = pPlayer.pLocation
    if DoesHaveItem(pItem, pPlayer):
        pLocation.tItems.append(pItem)
        pLocation.tCanPickup.append(True)
        pPlayer.tInventory.remove(pItem)
        print("Dropped the", pItem + ".")
    else:
        print("You don't have any", pItem + ".")
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

tCorridorNums = {pCorridor1W:51, pCorridor1E:50, pCorridor3W:45, pCorridor3E:42, pCorridor5W:48, pCorridor5E:40}
##
#GetWallsTotal
##
def GetWallsTotal():
    #We need to get the locations for the nav matrix since they move around... yeah that's what the buttons dooooo
    sumE = tCorridorNums[mLocations[30][2]] + tCorridorNums[mLocations[34][2]] - tCorridorNums[mLocations[38][2]]
    sumW = tCorridorNums[mLocations[30][3]] - tCorridorNums[mLocations[34][3]] + tCorridorNums[mLocations[38][3]]
    return sumE, sumW
##=======================
#DoExamine
#Prints the examine description and all items at the location
##=======================
def DoExamine(pLocation):
    print(tLocationsExamine[pLocation.i])
    print("You see a/an:")
    for i in pLocation.tItems:
        print("'" + i + "'")
    print()
    if pLocation == pCorridor6:
        iSumE, iSumW = GetWallsTotal()
        print("The east side has the number:", iSumE, "\nThe west side has the number:", iSumW)

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
        print("Gameover!\nThanks for playing!\n" + sMessage)
        sInput = input("Play Again? Y:N").lower()
        if "y" in sInput:
            return True
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
def Interpret(sInput, pPlayer, FunctionFrom): #Parameters can be reduced once the player becomes an object with methods that can get these for us
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
                sInput = input("Baby: Fine! What's you're name, dum-dum? ")
            
                if sInput == "Cornelius Marius Antonius, Pontifex Maximus... Roma":
                    pPlayer.pLocation = pCloset
                    print("Baby: What may I do for you?")
                    while not sInput == "end":
                        sInput = input ("Baby: Awaiting input...").lower()
                        if sInput == "give all items":
                            print("Baby: Everything, eh? Sure thing, Pontifex Maximus.")
                            pPlayer.tInventory.append(pBlockS)
                            pPlayer.tInventory.append(pBlockW)
                            pVoid.tItems.remove(pBlockS)
                            pVoid.tItems.remove(pBlockW)
                            pVoid.tCanPickup.pop()
                            pVoid.tCanPickup.pop()

                            pPlayer.tInventory.append(pBlockE)
                            pVoidN.tItems.remove(pBlockE)
                            pVoidN.tCanPickup.pop()

                            pPlayer.tInventory.append(pBlockN)
                            pVoidS.tItems.remove(pBlockN)
                            pVoidS.tCanPickup.pop()

                            pPlayer.tInventory.append(pHammer)
                            pPlayer.tInventory.append(pFlashlight)
                            pPlayer.tInventory.append(pMatches)
                            pCloset.tItems.remove(pHammer)
                            pCloset.tItems.remove(pFlashlight)
                            pCloset.tItems.remove(pMatches)
                            pCloset.tCanPickup.pop()
                            pCloset.tCanPickup.pop()
                            pCloset.tCanPickup.pop()

                            pPlayer.tInventory.append(pBatteries)
                            pOfficeSW.tItems.remove(pBatteries)
                            pOfficeSW.tCanPickup.pop()

                            pPlayer.tInventory.append(pRope)
                            pPlayer.tInventory.append(pMapOther)
                            pForest.tItems.remove(pRope)
                            pForest.tItems.remove(pMapOther)
                            pForest.tCanPickup.pop()
                            pForest.tCanPickup.pop()

                            pPlayer.tInventory.append(pDoll)
                            pLake.tItems.remove(pDoll)
                            pLake.tCanPickup.pop()

                            pPlayer.tInventory.append(pKey)
                            pPlayer.tInventory.append(pMap)

                                                    
                        
                        elif sInput == "disable mutators":
                            print("Baby: Of course, great lord!")
                            #TODO: PASS BOOLEAN THAT IS NEEDED FOR MUTATORS TO BE ACTIVE
                            #We can skip this since for now
                            pass
                        elif sInput == "set start":
                            sInput = input("Baby: ")
                            try:
                                sInput = int(sInput)
                                pPlayer.pLocation = tLocations[sInput]
                                print(pPlayer.pLocation.sDescLong)
                                print("It is done. How about you? I'm bored.")
                            except:
                                print("Idiot. Choose a row index on the navigation matrix.")
                                continue
                else:
                    pPlayer.pLocation = pCloset
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
##================================
#DetermineUse
#Figures out what to do based on input
##================================
def DetermineUse(sParam, pPlayer): #I'M LAZY CAN'T BE BOTHERED TO CHANGE THE PARAMETER TO MAKE SENSE

    pLocation = pPlayer.pLocation
    #We're going to have to go old school here
    if sParam == "Map":
        pass #Implement if there's time

    elif sParam == "Flashlight":
        #Did the player use the batteries?
                    
        if not tCanUse[3] and pFlashlight in pPlayer.tInventory:
        #Are they at the ravine?
            if pLocation.i in mCanUseAt[2]:
                    
                print("You turn on the flashlight, allowing you to see."
                        " See the huge drop before your feet, facing south, "
                        "that is. Now only if you had a way down...")
                tCanUse[2] = False #Turn it on once 
                tCanUse[5] = True #Can use the rope
                bDoesRavineKill = True
                pRavine.sDescLong = "You climb down the rope down into the ravine. Eventually you reach the bottom."
            else:
                    print("It works, but there's no reason to use it here.")
        elif pFlashlight in pPlayer.tInventory and tCanUse[3]:
            print("It needs batteries, it would seem.")
                        
    elif sParam == "Hammer":
            #Use one: is the player in the hallway and did not yet use the hammer?
            if pLocation == pHallway1 and tCanUse[4] and pHammer in pPlayer.tInventory:
                print("Using the hammer, you smash the glass casing, allowing you to access the map.")
                pLocation.tCanPickup[pLocation.GetItemIndex(pMapOffice)] = True
                tCanUse[4] = False
                #A listener for when the player reaches pElevator will reset tCanUse for pElevatorUp is needed
            #Use two: is the player in the elevator, did they go up, use examine, and not use the hammer?
            elif pLocation == pElevatorUp and tCanUse[4] and pLocation.bHasSearched and pHammer in pPlayer.tInventory:
                print("Taking the hammer, you smash through the canvas. You peer through and... "
                        " It's... an office. It's THE office. This canvas, upon a closer look, is the"
                        " back of chairman Bobbo!")
                #USE ReplaceLocation(WHERE r = pElevator SET c0 = pOfficeSE)
                        
                ReplaceLocation(pElevatorUp.i, 3, pOfficeSE)
                tCanUse[4] = False
    elif sParam == "Rope" and tCanUse[5]:
        #Can it be used here?
        if pLocation.i in mCanUseAt[2] and pRope in pPlayer.tInventory: #Shhhh 
            print("You tie the rope to the ledge and throw it down the ravine. Did it reach any bottom?")
            tCanUse[5] = False
            #bDoesRavineKill = False
            #Will no longer work since this is a function now
            #Instead I'm going to set the path to the elevator to be initially None
            #And then update it here once the player uses the rope
            #We simply have to check if the path to the elevator from the ravine is None
            #To see if it should kill the player of not
            ReplaceLocation(pRavine.i, 2, pElevator)
    elif sParam == "Matches":
        #Is the player in the deep cave and does the cave have the doll
        if pLocation == pCaveDeep and pDoll in pCaveDeep.tItems and pMatches in pPlayer.tInventory: # and iUses > 0:
            if tCanUse[10]:
                print("With the doll in the incantation circle, you light a match set it ablaze.",
                        "Eventually, once the flames die down, you find among the ashen remains a key.")
                iDoll = pLocation.GetItemIndex(pDoll)
                pLocation.tItems.pop(iDoll)
                pLocation.tCanPickup.pop(iDoll)
                pLocation.tItems.append(pKey)
                pLocation.tCanPickup.append(True)
                tCanUse[10] = False
            else: print("No reason to use that here.")
    elif sParam == "Batteries":
        #Just learned how to do DoesHaveItem in one line
        if pFlashlight in pPlayer.tInventory:
            print("You put the batteries in the flashlight.")
            pPlayer.tInventory.remove(pBatteries)
            tCanUse[3] = False #For use in flashlight check

    elif sParam == "Key":
        if pLocation == pOfficeS and pKey in pPlayer.tInventory:
            print("Using the key, you unlock the double doors.")
            tCanUse[11] = False
            #USE ReplaceLocation(WHERE r = pOfficeS SET c1 = pBossOffice
            ReplaceLocation(pOfficeS.i, 1, pCorridor1)
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
    bDoesRavineKill = True 
    bDoShowSequence = True
    
    while bGameState:
     #   bHasLight = DoesHaveItem(pFlashlight, tPlayerInventory)
        print(pPlayer.pLocation.GetLocationDescription())
        #Update pLocation
        UpdateLocation(pPlayer)
        sInput = input()
        sInput = sInput.lower().strip()
        #bVar1, sVar1, sVar2, iVar1, iVar2, sResult = Interpret(sInput, pLocation, iScore, iNumMoves, "Main")#This is going to get hideous
        #Now we just need to interpret the return values here by looking at sResult
        #if sResult is not none:
        #   if sResult is "setlocation":
        #        pLocation, iNumMoves, iScore = sVar1, iVar1, iVar2
        #That's all we have for now
        
        try:
            pLocation = pPlayer.pLocation
            sCommand, sParam = sInput.split()
            sParam = sParam.capitalize()
            if sCommand == "take":
                
                if pLocation.bHasSearched == True:
                    
                    Pickup(pPlayer, sParam)
                else:
                    iPickup = 0
                    for i in range(len(pLocation.tItems)):
                        if pLocation.tCanPickup[i]:
                            iPickup += 1
                    if iPickup > 0:
                        if pLocation.tCanPickup[pLocation.GetItemIndex(sParam)]:
                            Pickup(pPlayer, sParam)
            
            elif sCommand == "drop":
                Drop(pPlayer, sParam)

            elif sCommand == "use":

                #This could've been a function. Oh well.
                #IT IS NOW, LOOK AT ALL THE WHITE SPACE!
                DetermineUse(sParam, pPlayer)
                        
                        
                        

        #The command is one word or more than two words
        except ValueError:
            
            if sInput == "north":
                pPlayer.pLocation = SetLocation(pPlayer, 0) #0 = North

            elif sInput == "south":
               pPlayer.pLocation = SetLocation(pPlayer, 1) #1 = South
    
            elif sInput == "east":
                pPlayer.pLocation = SetLocation(pPlayer, 2) #2 = East

            elif sInput == "west":
                pPlayer.pLocation = SetLocation(pPlayer, 3) #3 = West

            elif sInput == "up":
                pPlayer.pLocation = SetLocation(pPlayer, 4) #4 = Up
            elif sInput == "down":
                pPlayer.pLocation = SetLocation(pPlayer, 5) #5 = Down
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
                      "Take: Take the specified item found at location with examine.\n"
                      "Drop: Drops the specified item in your inventory\n"
                      "Use: Uses the specified item in your inventory\n"
                      "Inventory: Shows your inventory.")

            elif(sInput == "quit"):
                sInput = input("This will end the game and count as a game over. Continue?\n" #Changing sInput shouldn't cause issues
                           "<Enter 'y' for 'yes or 'n' for no'>\n")
                sInput = sInput[0].lower()

                if(sInput == "y"):
                    Copyright(pPlayer, True)
                    return True #The player chose to play again

            elif(sInput == "map"):
                
                #Does the player HAVE a map?
                if DoesHaveItem(pMap, pPlayer) or pPlayer.pLocation.i < 6:
            
                    if pPlayer.pLocation.i > 5 and pPlayer.pLocation.i < 27: #Always plan for the future... not that I have anything planned
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
                DoExamine(pPlayer.pLocation)
                pPlayer.pLocation.bHasSearched = True
                for i in range(len(pPlayer.pLocation.tItems)):
                    #Special circumstance items that need more than just examining the location to pick anything up
                    if not (pPlayer.pLocation.tItems[i] == pMapOffice or pPlayer.pLocation.tItems[i] == pKey):
                        pPlayer.pLocation.tCanPickup[i] = True
                        
                        
            
            #if not DoesHaveItem(tLocationsItem[i], tPlayerInventory): 
            #    tCanPickup[i] = True
                
            elif sInput == "look":
                print(pPlayer.pLocation.sDescLong)

            elif sInput == "take":
                print("Take what?")
                pLocation = pPlayer.pLocation
                if pPlayer.pLocation.bHasSearched == True:
                    
                    for i in pLocation.tItems:
                        print(i)
                    if len(pLocation.tItems) > 0:
                        sInput = input().capitalize().strip()
                        Pickup(pPlayer, sInput)
                else:
                    #There may situations where a player has dropped an item somewhere but not searched that area
                    #Do the above, but only show items that can already be picked up AKA they were dropped there
                    iPickup = 0
                    for i in range(len(pLocation.tItems)):
                        if pLocation.tCanPickup[i]:
                            iPickup += 1
                            print(pLocation.tItems[i])
                    if iPickup > 0:
                        sInput = input().capitalize().strip()
                        i = pLocation.GetItemIndex(sInput)
                        if i:
                            if pLocation.tCanPickup[i]:
                                Pickup(pPlayer, sInput)
                            
            elif sInput == "drop":
                if len(pPlayer.tInventory) > 0:
                    print("Drop what?\nInventory:\n===========")
                    for i in pPlayer.tInventory:
                        print(i)
                    print()
                    sInput = input().capitalize().strip()
                    Drop(pPlayer, sInput)
                else:
                    print("You have nothing to drop!")

            elif sInput == "inventory":
                print("Inventory:\n===========")
                for i in pPlayer.tInventory:
                    print(i)

            elif sInput == "use":
                print("Use what?\nInventory:\n===========")
                for v in pPlayer.tInventory:
                    print(v)
                sInput = input().capitalize().strip()
                DetermineUse(sInput, pPlayer)
            else:
                print("Command not valid")
        ##LOCATION MUTATORS
        #Did the player enter the center of the office?
        if pPlayer.pLocation == pOfficeC:
            SwitchLocations(pOfficeW.i, 3, pOfficeE.i, 2)
        #Did the player go to the lake?
        elif pPlayer.pLocation == pLake:
            
            #Unblock Cave
            ReplaceLocation(pWaterfall.i, 2, pCaveEnt)

        #Did the player go to the waterfall before going to the lake?
        elif pPlayer.pLocation == pWaterfall:
            if pLake.bHasVisited == False:
                
                #Block the lake
                ReplaceLocation(pRiver.i, 3, pWaterfallTop)
        #Did the player go to the Forest?
        elif pLocation == pForest:
            #Is the Lake blocked?
            if mLocations[pRiver.i][3] == pWaterfallTop:
                #Unblock the Lake
                ReplaceLocation(pRiver.i, 3, pLake)
        
        ##ENDINGS
        #End of tutorial
        if pPlayer.pLocation.i < 6:
              if pBlockN in pVoidN.tItems and pBlockS in pVoidS.tItems and pBlockE in pVoidE.tItems and pBlockW in pVoidW.tItems:
              
            
               bGameState = False
               print(pPlayer.pLocation.GetLocationDescription())
               return bGameState

        #Reaching move limit
        elif pPlayer.iMoves > 60 and pPlayer.Location.i > 5 and bDoShowSequence:
            print(pPlayer.pLocation.GetLocationDescription())
            print("\nBaby: Well, you certainly seem to be underperforming. It's quite boring actually. "
                  "SERIOUSLY, what could be taking you so long?")
            #If the player is missing this item, end the game
            if not DoesHaveItem(pKey, pPlayer):
                bGameState = False
                print("Baby: Whatever. Nap time!")
                return bGameState
                
            else:
                print("Baby: Mm. You're close, I'll give you that. Don't. Waste. My. Time.")
                bDoShowSequence = False
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

        #New Ending
        elif pPlayer.pLocation == pChairOffice:
            if pKey in pPlayer.pLocation.tItems:
                print("Baby: Thank you. Have a seat.")
                print("Baby: you see,", pPlayer.sName, "You've done a lovely job getting here.")
                print("Baby: I get most people with the Broom Closet! Anyways, thanks for playing!")
                print("\nYou scored", pPlayer.iScore, "in", pPlayer.iMoves, "moves.")
                input("Nice? ")
                print("Baby: What's that? Where are you? Why are you? What am I?")
                print("Baby: Pffft, I dunno!") #I dunno
                bGameState = False
                return bGameState
            else:
                print("Baby: Welcome, Welcome! Ah, so you brought Bobbo his key! Leave it on the desk, will ya?")
                #Drop the key
            
        #My favorite ending
        elif pPlayer.pLocation == pCloset and pPlayer.iMoves > 5:
            bGameState = False
            print(pPlayer.pLocation.GetLocationDescription())
            print("Suddenly the door slams shut behind you. You go to open it, only for the handle to fall off.")
            print("Baby: Eh, did you get the Broom Closet Ending? The Broom Closet Ending is my favourite!") #I spelt favourite like that intentionally by the by
            return bGameState
        #Fell down the Ravine ending
        elif pPlayer.pLocation == pRavine and mLocations[pRavine.i][2] == None:
            bGameState = False
            print(pLocation.GetLocationDescription())
            print("\nBaby: Oops, looks like someone found their mortality!")
            return bGameState
        

b = Init()
while b:
    print(b)
    b = Init()
