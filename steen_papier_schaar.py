# this is my second project (hangman)

import random 

list = (["steen","papier","schaar"])
opnieuw = True
player = None
computer = (random.choice(list))

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
        opnieuw = False

print("bedankt voor het spelen")