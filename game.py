# Intro to Programming
# Author: Anthony Griggs
# Date: 9/12/17

#Project2
#Ver 0.3 9/25/17


gLocVoid = ("You awake to find a white empty space. You seem to be floating in an exetensial 'nothingness'."
            "A chill runs down your spine: what exactly is this place, this unfamiliar void that you find yourself imprisoned within?")
            #
gLocVoidN = ("You follow one of the lines to a circle that, upon investigation, has the letter 'N' on it.")
gLocVoidS = ("You follow one of the lines to a circle that, upon investigation, has the letter 'S' on it.")
gLocVoidE = ("You follow one of the lines to a circle that, upon investigation, has the letter 'E' on it.")
gLocVoidW = ("You follow one of the lines to a circle that, upon investigation, has the letter 'W' on it.")
            #
gLocSegun = ("Suddenly the empty void is replaced in an instant with the hubris of a city street!"
            "Your mind races to find an answer, to find some logical reasoning as for what is going on here!"
            "There is nothing. A sense of panic and fear begins creep from within.")
            #
gLocTrice = ("Old, rusted cars litter the streets; most buildings -- those that still are standing -- are overgrown with moss, as nature reclaims what it once lost."
            "You can't get over the insanity of it all! What's going on? Suddenly you come across what appears to be a central plaza."
            "It's then you notice it's littered with human remains. Everywhere you look, the bones of what you assume to be the long deceased."
            "But... wait! There weren't any remains anywhere else you saw! That little fact makes this all the more perplexing!"
            "You need answers! SOME DAMN SANITY FOR ONCE! You cry out in frustration and fear.")
            #
gLocFinal = ("Suddenly you are in a room. The floor is encompassed with a soft gray carpet. In the corner you see a bed with a nightstand beside it."
            "The bed is made, and it looks unused. The walls are painted a sleek, bright red, but... wait a second. There are no windows! There's no door!"
            "There's no way in or out! You've been trapped.")
            #
gLocStart = ("You awake to find a white empty space. You seem to be floating in an exetensial 'nothingness'."
            "A chill runs down your spine: what exactly is this place, this unfamiliar void that you find yourself imprisoned within?")
            #
gLocSegun = ("Suddenly the empty void is replaced in an instant with the hubris of a city street!"
            "Your mind races to find an answer, to find some logical reasoning as for what is going on here!"
            "There is nothing. A sense of panic and fear begins creep from within.")
            #
gLocTrice = ("Old, rusted cars litter the streets; most buildings -- those that still are standing -- are overgrown with moss, as nature reclaims what it once lost."
            "You can't get over the insanity of it all! What's going on? Suddenly you come across what appears to be a central plaza."
            "It's then you notice it's littered with human remains. Everywhere you look, the bones of what you assume to be the long deceased."
            "But... wait! There weren't any remains anywhere else you saw! That little fact makes this all the more perplexing!"
            "You need answers! SOME DAMN SANITY FOR ONCE! You cry out in frustration and fear.")
            #
gLocFinal = ("Suddenly you are in a room. The floor is encompassed with a soft gray carpet. In the corner you see a bed with a nightstand beside it."
            "The bed is made, and it looks unused. The walls are painted a sleek, bright red, but... wait a second. There are no windows! There's no door!"
            "There's no way in or out! You've been trapped.")

cont = "<Press enter to "
#sName = "" #Unecessary
#TODO:  *UPHEAVAL - I consider this an interactive demo. I feel the game itself will be much different. It'll have a completely different story, I mean
#       *Distinct different kinds of texts - Descriptions, player dialogue, Program dialogue, etc.
#       *dprint(...) when the time comes
#       *Baby
#       *Tables with specific texts
#       *Table that specializes in interpretting vulgar language from inputs. Yeah I'm already planning for that
#       *On new branch: Dialogue choices for player! Add a bit of flair, personality via choice while still staying rather linear
#       *Get in to objects
#       *Get rid of this killer headache
#       *HAVE FUN!!!
#       *etcetera

#def IncScore(i):
#   i = i + 5
#    return i

    
def init(): #Initialization function, runs when the code is run
    print("*********   *********      ***      *           *********   *********   *       *\n"
          "*       **  *              * *      *               *           *        *     *\n"
          "*        *  *             ** **     *               *           *         *   *\n"
          "*       **  *             *   *     *               *           *          * *\n"
          "*********   *********    *******    *               *           *           *\n"
          "*       **  *            *     *    *               *           *           *\n"      
          "*        *  *           **     **   *               *           *           *\n"           
          "*        *  *********   *       *   *********   *********       *           *\n")     
    pLocation = gLocStart #Change to function call once function is defined
    #Begin introduction
    print(gLocStart)      
    input("input: ") #Ignore first input
    print("???: Hey! Can you hear me?")
    input(cont + "continue>") #Must use concatenation for input
    print("???: Good. Now, I know you must have plenty of questions, such as where you are, or who I am. We'll get to them when the time comes.\n"
          "\n"
          "???: There are more pressing matters. Protocol states that I must perform a sitrep on your state of being before we can adress any inquiries.\n"
          "Understand?")
    input(cont + "understand>")
    sName = input("???: First things first: do you know your name?\n"
                  "Your name? ")
    
    print("???: " + sName + "? All right. Now let's see about your sense of orientation.\n"
          "\n"
          "Suddenly a red circle appears beneath your feet. You notice four lines spreading outward from it in four directions, leading to other circles\n"
          "\n"
          "???: Okie-dokie, go ahead and walk towards any of these circles. I know you're confused, but stick with me. If you feel you need help, just say the word.\n"
          "<Type 'North', 'South', 'East', or 'West' to head in that direction. To see all commands availible to you, type 'Help'>\n")
    #Update pLocation to showcase changes made
    pLocation = ("You awake to find a white empty space. You seem to be floating in an exetensial 'nothingness'."
                "A red circle with four lines leading in four directions to four other circles appears under your feet.")
    #Enter the gamestate
    main(pLocation, sName, True)
    return sName #Send to global variable.
    
    
    
#####
#main
#Gamestate function, always active while player is in the game
#Parameters:
#   *sLocation, the location to start the game at
#   *sName, the name the player chose (Although init does pass sName as a global, it can't be done until the end of the function. Therefore main must rely on it locally)
#   *bFirstRun, indicate whether or not this is the first instance of firing the loop (In other words, decide if it a part of the intro or not)
#####
def main(sLocation, sName, bFirstRun):
    pLocation = sLocation
    if(bFirstRun == True):
        bCanNorth = True
        bCanSouth = True
        bCanEast = True
        bCanWest = True
        #This solution isn't permanent
        # We need to set these based on the location the player is at
        #   Thus, we need to be able efficiently check the location once in the if statements
        # But for now, it'll get job done
    while True:
        print(pLocation)
        sInput = input()
        sInput = sInput.lower()
        if(sInput == "north" or sInput == "south" or sInput == "east" or sInput == "west"):
            if(sInput == "north" and bCanNorth == True): 
                if(pLocation != gLocVoidS): #Remember, the command was north, so the location should be the opposite
                    pLocation = gLocVoidN
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
                
        
        

sName = init()
    

