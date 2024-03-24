# Steven Holmes
# COP 2500
# Travel Adventure
# January 27, 2023

#You were experimenting with teleportation devices in the lab for research.  The primary issue is that onece the teleportation devices start to generate power, there is no way 
#to stop them from manifesting.  This research can essentially make anything work as a teleporting device, similarly to a portkey.  The room where the teleportation device is housed
#is sealed off from the rest of the lab, but will teleport anything within the enclosed room.  You set up the device that would be the delivery sight for the telported object, in this
#case, you are using an inanimate object.  That object being a toy replication of a ride vehicle for Hagrid's Magic Motorbike Adventure.  Once you started the activation of the device,
#you glanced down at your notes and started to notice there was a miscalculation.  But it was too late, the device had already started to draw power, unable to shut it down, the 
#consequences were not yet known.  You glance through the enclosed glass room, over to the monitor and see the power generation was approaching 95%.  You can't risk opening the room,
#and possibly creating a localized blachole in the lab, sucking everything into it.  How could this have gone so wrong?  What was supposed to be a simple teleportation of Hagrid's ride vehicle
#into the adjacent room, was now turning out to be a real nightmare.  The room went so white, you could no longer see anything.  You didn't know if you were still in the lab or where you were.
#Everything went black as you felt your body becoming so compressed, you couldn't breathe.  "Is this what happens in death? Am I even alive?  I must be, I can still have thoughts."  You lose
#consciousness.  Next thing you know, you open your eyes and you are somehwere you don't recognize.  You turn back and see skyscrapers in ruin.  Being overtaken by nature.  You don't know
#if you are on earth, or on another planet in another dimension.  You don't know if you time traveled to the future of your earth or the past of another planets reality.  You head towards what's 
# left of the city thinking you may be able to find a newspaper.  When you do, you see at the top of the paper "OLD YORK ETERNITY" and the cover shows a picture of the bay area, but where you
#expected to see Lady Liberty, you see what you recognize as the Eiffel Tower.  Then, glancing back up towards the top you see the year 200.  Not only did you travel to another dimension,
#you have also traveled to a time in which there is no correlation to what you remember as 2023.  Or so you think.  All you have with you is Hagrid's Motorbike RV toy and your calculations.
#The teleportation device desolves back to where it came from leaving just you and the other objects in the room at your departure.  You will need to figure out how to fix your calculations
#and somehow turn Hagrid's Motorbike into the teleportation device you need to get yourself home.  You will be asked some questions that will help guide you to wherever you call home. Good Luck!

print("You must make the decision on whether you want to stay and make a life in this world, or fix your calculations and find your way back home.")
print("So which will it be?  Do  you want to stay and rule this planet, or return home?")
print("If you want to stay, enter \"Stay\", but if you want to return home enter \"Phone Home\"")
destination = input()

if (destination=="Stay"):
    print("I don't know about this, but you're the one making the decisions. \
First we need to locate some supplies.")
    print("You walk into the first building you find a door, but it has a key code lock on it, \
let's see if you can guess the passcode")
    print("You will be given a riddle to hint at each number,\
you have unlimited guesses, if you don't figure this out, you're stuck forever anyways.")

    hidden_value_1 = int(3)
    hidden_value_2 = int(9)
    hidden_value_3 = int(6)
    hidden_value_4 = int(4)
    guess_1 = -1
    guess_2 = -1
    guess_3 = -1
    guess_4 = -1

    while (guess_1 != hidden_value_1):
        guess_1 = int(input("Hint: Around the tree, around the tree now we have: Which number?\n"))

        if guess_1 != hidden_value_1:
            print("Remember, unlimited tries... go again.")
        else:
            print("Okay, we move to the next one")


    while (guess_2 != hidden_value_2):
        guess_2 = int(input("First you make a circle, then you add a line: Which number do we have?\n"))

        if guess_2 != hidden_value_2:
            print("Remember, unlimited tries... go again.")
        else:
            print("Great!  Halfway there, keep going.")

    while (guess_3 != hidden_value_3):
        guess_3 = int(input("Curve around until it sticks: Which number do we have?\n"))

        if guess_3 != hidden_value_3:
            print("Remember, unlimited tries... go again.")
        else:
            print("So close, we just need one more!")

    while (guess_4 != hidden_value_4):
        guess_4 = int(input("Down and across and down some more: Which number do we have?\n"))

        if guess_4 != hidden_value_4:
            print("Remember, unlimited tries... go again.")
        else:
            print("GREAT!  You have figured it out.  The door has opened!")
    print("Beyond the door is an odd creature, he tells you if you can solve his riddle \
    he has enough supplies to last you 10 years.")
    print("You will get a hint and 2 guesses before given another hint in which you will get two more guesses, \
    if you fail to guess the word, you will be stranded here until you perish! **make evil laugh sound in your head**")

    x = 0
    y = 2
    guess = str("hey")

    while (x<y and guess != "Alphabet"):
        x=x+1
        guess = input("The first riddle: What word contains all of the twenty-six letters?\n")

        if guess == "Alphabet":
            print("Great job! You did it! You will rule you're own world!")
        else:
            print("Not even close")

    chances = 2
    guess = str("Hey")
    while (chances>0 and guess != "Alphabet"):
        chances = chances -1
        guess = input(("Your second hint is: What contains the letters within a language?\n"))

        if guess == "Alphabet":
            print("Great job! You did it! You will rule you're own world!")
        else:
            print("Not even close.  It is sad that you will now perish here for all eternity!  Your adventure stops here!")

elif destination == "Phone Home":
    print("Okay, we better figure this calculation quickly")
    print("You are wandering the city looking for clues and you stumble across the parallel version of the lab you had been working \
working with in your previous timeline.  You power on the computer and are confronted with a question to unlock it. \"What is your wife's maiden name?"\")

