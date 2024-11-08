in my third project I made a gallows game where you can guess multiple words and it can also end in a game over enjoy !!!

import random

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('welcom by the hangman game !!')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
 
list = (["steen","papier","schaar"])
opnieuw = True 

while opnieuw:

    player = None
    computer = (random.choice(list))

    while player not in list:
        player = input("maak een keuze ! (steen, papier, schaar) ")

    print(f"player:{player}")
    print(f"computer:{computer}")

    if player == computer:
        print("that a tie ")
    elif player == "steen" and computer == "schaar":
        print("you won")
    elif player == "papier" and computer == "steen":
        print("you won")
    elif player == "schaar" and computer == "papier":
        print("you won")
    else:
        print("you lose")

    if not input("wil je opnieuw splen?? (y/n)").lower() == "y":
        break 

print('bedankt voor het spelen')
