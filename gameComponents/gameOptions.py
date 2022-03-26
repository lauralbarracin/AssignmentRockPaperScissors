from gameComponents import gameVars
from random import randint

def gameOptions():
    print ("==========*  R  O  C K  - P A P E R - S C I S S O R S **  THE ORIGINAL GAME *=======")
    print (" ^^ DO YOU BELIEVE IN LUCK?  You will need it if you want to play this game *_*")
    print ("You will have three (3) lives during this traditional game. Now is your turn... Choose a weapon: R - O - C - K *  P- A - P -E - R * S - C - I -S S O R S")
    print("Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
    print("Player Lives:", gameVars.player_lives, "/", gameVars.total_lives)
    print("=============================================================================")
    print("Choose your weapon!  Rock  * Paper * Scissors * Or Type quit to exit\n") #\n means "new line"
    gameVars.player_choice = input("Choose rock, paper, or scissors: \n")

    if gameVars.player_choice == "quit":
        print("You choose to quit. However, the moment you want to quit, is the moment when you need to keep pushing")
        exit ()

    print("user chose: " + gameVars.player_choice)

    gameVars.computer_choice = gameVars.choices[randint(0, 2)]

    print("computer chose: " + gameVars.computer_choice)

    if gameVars.computer_choice == gameVars.player_choice:
        print ("tie")

    elif gameVars.computer_choice == "rock":
        if gameVars.player_choice == "scissors":
            print ("you lose!. I told you, you need luck -.- ")
            gameVars.player_lives -= 1
        else:
            print ("you win!. Amazing, you did great ^^")
            gameVars.computer_lives -=1

    elif gameVars.computer_choice == "paper":
        if gameVars.player_choice == "scissors":
            print ("you win!. Amazing, you did great ^^")
            gameVars.computer_lives -= 1
        else:
            print("you lose!. I told you, you need luck -.- ")
            gameVars.player_lives -= 1

    elif gameVars.computer_choice == "scissors":
        if gameVars.player_choice == "paper":
         print("you lose!. I told you, you need luck -.- ")
         gameVars.player_lives -= 1
        else:
         print("you win!. Amazing, you did great ^^")
        gameVars.computer_lives -= 1

    gameVars.player_choice = False

