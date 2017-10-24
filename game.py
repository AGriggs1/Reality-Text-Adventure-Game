# Intro to Programming
# Author: Anthony Griggs
# Date: 9/12/17

#Project2
#Ver 0.3 9/25/17

from time import sleep # :)
import sys #Learned about this from https://stackoverflow.com/questions/949504/terminating-a-python-program









gHelp = ("List of commands:\n"
        "North: moves player in the 'north' direction.\n"
        "South: moves player in the 'south' direction.\n"
        "East: moves player in the 'east' direction.\n"
        "West: moves player in the 'west' direction.\n"
        "Help: displays a list of commands. Hey, a dictionary's gotta have the definition of a dicitionary in it.\n"
        "Quit: ends the game. Considered a game over.\n")

gLocVoid = ("You awake to find a white empty space. You seem to be floating in an exetensial 'nothingness'."
            "A chill runs down your spine: what exactly is this place, this unfamiliar void that you find yourself imprisoned within?")
            #
gLocVoidN =("You follow one of the lines to a circle that, upon investigation, has the letter 'N' on it."
            "The area around you transforms into a forest filled teeming monstrous redwood trees. You hear the songs of various birds, and feel welcome.")
            #
gLocVoidS = ("You follow one of the lines to a circle that, upon investigation, has the letter 'S' on it. The area around you transforms."
             "Suddenly you are at the edge of a cliff overlooking the open sea. You hear the waves crashing against the crags below you, "
             "smell the mist of saltwater, and feel a sense of somberness.")
            #
gLocVoidE = ("You follow one of the lines to a circle that, upon investigation, has the letter 'E' on it. The area around you transforms and you are on the streets of a city that seems to be long abandoned. "
             "Cars rusted, buildings crumbling, overgrown with moss and vines. You can't help but feel curious about the fate of this place.")

gLocVoidW = ("You follow one of the lines to a circle that, upon investigation, has the letter 'W' on it. The area around you transforms into an office."
             "Desks teeming with paperwork and the faint smell of morning coffees makes you anxious. ")
            #

gLocFinal = ("The void disappears and suddenly you are in free fall. You look down to see the gaping maw of a great, big volcano, it's molten rock spewing and spitting, "
             
             "eager to consume you entirely. You are burned alive.") #Great way to ends things yeah?

cont = "<Press enter to "
bDevMode = True

#TODO:  *Distinct different kinds of texts - Descriptions, player dialogue, Program dialogue, etc.
#       *dprint(...) when the time comes
#       *Tables with specific texts
#       *Table that specializes in interpretting vulgar language from inputs. Yeah I'm already planning for that
#       *On new branch: Dialogue choices for player! Add a bit of flair, personality via choice while still staying rather linear
#       *Get in to objects
#       *HAVE FUN!!!
#       *etcetera



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
    pLocation = gLocVoid #Change to function call once function is defined
    #Begin introduction
    print(gLocVoid)      
    input("input: ") 
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
    pLocation = ("You find yourself in some sort of white void, some, 'nothingness'."
                "A red circle with four lines leading in four directions to four other circles appears under your feet.")
    #Enter the gamestate for the first time
    #SO I REMEMBER: in tLocScore, first index is location, second is score
    tLocScore = Main(pLocation, sName, iScore, True) #We need to send pLocation back to init(), don't we? I'll have to think about implementing that #SOLVED leaving so you can probe my thought process
    #Begin second half of in intro
    print("???: Excellent, " + sName + ". You seem to be in optimal shape. Excellent indeed.\n"
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
    print("Baby: This test is not optional! Don't worry, " + sName + " you're in sA@e Ha@dS\n"
          "Baby: Let's g#t sta$%$\n")
    pLocation = gLocFinal
    print(gLocFinal) #ENDING WITH A BANG
    Copyright(tLocScore[1], True)
    
    
    
    #return sName #Send to global variable. #NEVER GETS USED

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
        sys
    print(sMessage)

    
##==========================================
#Interpret
#Takes user input and decides what to do
#Parameters:
#   sInput, the player input to read
#   iScore, the player's score
#   FunctionFrom, the function Interpret is being called from. This will likely be a short string
##==========================================
def Interpret(sInput, iScore, FunctionFrom):
    sInput = sInput.lower()

    if bDevMode and sInput[0:4] == "dev:":
        print("Developer mode active. Developer command detected.")
        sInput = sInput[3:len(sInput)] #Go ahead and cut off the first 'dev:' since we already checked that
        #TODO: If statements for commands go here

    #Consider spliting up a string by spaces and interpreting every word in it
        if sInput == "north":
            pass

        elif sInput == "south":
            pass

        elif sInput == "east":
            pass

        elif sInput == "west":
            pass

        elif sInput == "help":
            print(gHelp) #I feel globals are okay IF they are intended to not be changed by the program

        elif sInput == "quit":
            sInput = input("This will end the game and count as a game over. Continue?\n" #Changing sInput shouldn't cause issues
                  "<Enter 'y' for 'yes or 'n' for no'>\n")
            sInput = sInput[0].lower()

            if(sInput == "y"):
                Copyright(iScore, True)
                return False, iScore #For use in main?
    
    #Also reworking if statment logic while we're at it
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
def Main(sLocation, sName, iScore, bFirstRun):
    pLocation = sLocation
    bGameState = True

    if(bFirstRun == True):
        bCanNorth = True
        bCanSouth = True
        bCanEast = True
        bCanWest = True
        #
        bVisitedVoid = True
        bVisitedVoidN = False
        bVisitedVoidS = False
        bVisitedVoidE = False
        bVisitedVoidW = False
        #This solution isn't permanent
        # We need to set these based on the location the player is at
        #   Thus, we need to be able efficiently check the location once in the if statements
        # But for now, it'll get the job done
    while bGameState:
        print("Your score:", iScore)
        print(pLocation)
        sInput = input()
        sInput = sInput.lower()

        if(sInput == "north" or sInput == "south" or sInput == "east" or sInput == "west"):

            if(sInput == "north" and bCanNorth == True): 

                if(pLocation != gLocVoidS): #Remember, the command was north, so the location should be the opposite
                    pLocation = gLocVoidN

                    if(bVisitedVoidN == False):
                        iScore = iScore + 5
                        bVisitedVoidN = True
                    bCanNorth = False
                    bCanSouth = True
                    bCanEast = False
                    bCanWest = False

                else:
                    pLocation = sLocation
                    bCanNorth = True
                    bCanSouth = True
                    bCanEast = True
                    bCanWest = True

            elif(sInput == "south" and bCanSouth == True):

                if(pLocation != gLocVoidN):
                    pLocation = gLocVoidS

                    if(bVisitedVoidS == False):
                        iScore = iScore + 5
                        bVisitedVoidS = True
                    bCanNorth = True
                    bCanSouth = False
                    bCanEast = False
                    bCanWest = False

                else:
                    pLocation = sLocation
                    bCanNorth = True
                    bCanSouth = True
                    bCanEast = True
                    bCanWest = True

            elif(sInput == "east" and bCanEast == True):

                if(pLocation != gLocVoidW):
                    pLocation = gLocVoidE

                    if(bVisitedVoidE == False):
                        iScore = iScore + 5
                        bVisitedVoidE = True
                    bCanNorth = False
                    bCanSouth = False
                    bCanEast = False
                    bCanWest = True

                else:
                    pLocation = sLocation
                    bCanNorth = True
                    bCanSouth = True
                    bCanEast = True
                    bCanWest = True

            elif(sInput == "west" and bCanWest == True):

                if(pLocation != gLocVoidE):
                    pLocation = gLocVoidW

                    if(bVisitedVoidW == False):
                        iScore = iScore + 5
                        bVisitedVoidW = True
                    bCanNorth = False
                    bCanSouth = False
                    bCanEast = True
                    bCanWest = False

                else:
                    pLocation = sLocation
                    bCanNorth = True
                    bCanSouth = True
                    bCanEast = True
                    bCanWest = True

            else:
                print("You can't go that way.")

        elif(sInput == "help"):
            print("List of commands:\n"
                  "North: moves player in the 'north' direction.\n"
                  "South: moves player in the 'south' direction.\n"
                  "East: moves player in the 'east' direction.\n"
                  "West: moves player in the 'west' direction.\n"
                  "Help: displays a list of commands. Hey, a dictionary's gotta have the definition of a dicitionary in it.\n"
                  "Quit: ends the game. Considered a game over.\n")#AKA run the game over/copyright function on quit

        elif(sInput == "quit"):
            sInput = input("This will end the game and count as a game over. Continue?\n" #Changing sInput shouldn't cause issues
                  "<Enter 'y' for 'yes or 'n' for no'>\n")
            sInput = sInput[0].lower()

            if(sInput == "y"):
                Copyright(iScore, True)
                break

        else:
            print("Command is not valid.")

        if(bVisitedVoid == True and bVisitedVoidN == True and bVisitedVoidS == True and bVisitedVoidE == True and bVisitedVoidW == True): #Makes more sense down here
            print("Your score:", iScore) #Realised that a copy of this is needed here too 
            print(pLocation)
            bGameState = False 
            
    tLocScore = []
    tLocScore.append(pLocation)
    tLocScore.append(iScore)
    return tLocScore
        

Init()
    

