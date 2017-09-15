# Intro to Programming
# Author: Anthony Griggs
# Date: 9/12/17

gLocStart = "You awake to find a white empty space. You seem to be floating in an exetensial 'nothingness'. A chill runs down your spine: what exactly is this place, this unfamiliar void that you find yourself imprisoned within?"
gLocSegun = "Suddenly the empty void is replaced in an instant with the hubris of a city street! Your mind races to find an answer, to find some logical reasoning as for what is going on here! There is nothing. A sense of panic and fear begins creep from within."
gLocTrice = "Old, rusted cars litter the streets; most buildings -- those that still are standing -- are overgrown with moss, as nature reclaims what it once lost. You can't get over the insanity of it all! What's going on? Suddenly you come across what appears to be a central plaza. It's then you notice it's littered with human remains. Everywhere you look, the bones of what you assume to be the long deceased. But... wait! There weren't any remains anywhere else you saw! That little fact makes this all the more perplexing! You need answers! SOME DAMN SANITY FOR ONCE! You cry out in frustration and fear."
gLocFinal = "Suddenly you are in a room. The floor is encompassed with a soft gray carpet. In the corner you see a bed with a nightstand beside it. The bed is made, and it looks unused. The walls are painted a sleek, bright red, but... wait a second. There are no windows! There's no door! There's no way in or out! You've been trapped."
#def IncScore(i):
#   i = i + 5
#    return i
def main():
    #My, my
    pLocation = "NULL"
    
    #Set beginning location, run first sequence
    iScore = 0 #For some reason iScore doesn't work outside the function... 
               #No biggie, since I realized we'll want to reset it on every function call
    pLocation = gLocStart
    print("Score:", iScore)
    print()
    print(pLocation)
    print()
    print("Ah, some brain activity!")
    print("Well, well, look who's awake! Hey! Can you here me?")
    print()
    input("<Press enter to awake>")
    
    #Well, well
    #Second (Segun) sequence, setting new location 
    iScore = iScore + 5
    pLocation = gLocSegun
    print("Score:", iScore)
    print()
    print(pLocation)
    print()
    print("Whoa, that got you stirring, now didn't it? Hah! I sense you are confused. What is this place? Where might you be? Who am I? Where am I? What am I? These are great questions, but now's not the time. Soon you will understand.")          
    print("Take a look around.Then we'll talk. Understand?")
    print()
    print("<Press enter to understand>")
    
    #Third (Trice) Sequence, setting new location
    iScore = iScore + 5
    pLocation = gLocTrice
    print("Score:", iScore)
    print()
    print(pLocation)
    print()
    print("Well, well, well, what happended here? Hmhmhm...")
    print("Ah I do love the pain you feel! So beautiful! So emotional! So... human...")
    print("...")
    print("This... this is your world.")
    print("Understand?")
    print()
    input("<Press enter to understand>")
    #Player is responding NOTE: Add way to distinct player dialogue from location description and program dialogue
    input("No! Impossible!")
    print("Quite possible. You just don't remember. Understand?")
    print()
    input("<Press enter to understand>")
    input("That's not possible! I refuse to believe it! WHO ARE YOU?")
    print("Who am I? Irrelevant. Who are you? Come on, dum-dum, answer the question. Prove me wrong.")
    print()
    sName = input("Who are you? ")
    print(sName + "? No. No no. You don't even know your own name! Alright, enough games. Let's get to business.")

    #Final (Final) sequence, setting new location
    iScore = iScore + 5
    pLocation = gLocFinal
    print("Score:", iScore)
    print()
    print(pLocation)
    print()
    print("Ah, much better. See? You don't have to worry about what lies beyond these walls. I'll protect you! I'll keep you safe. Understand?")
    input("<Press enter to understand>")
    input("No. You want answers!")
    print("No. You want to be safe!\n" #Finna start using this method more 
          "I will keep you safe!\n"
          "You have to stay here, forever! Understand?")
    print()
    input("<Press enter to understand>")
    input("Safe? Is this some kind of game to you? Stop messing with me!")
    print("Game? What game? This is very real. I am going to break you. And you will comply. Can't you see what I can do? There's no fighting it. You will break. You will die.\n"
          "...\n"
          "Understand?")
    input("<Press enter to break>")
    print("Game over!")
    print("Score:", iScore)
    

main()
    

