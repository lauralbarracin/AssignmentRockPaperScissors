from gameComponents import gameVars
from random import randint

def game_options():
    print ("===============*/RPS GAME */==================")
    print("Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
    print("Player Lives:", gameVars.player_lives, "/", gameVars.total_lives)
    print("===============================================")
    print("Choose your weapon! Or Type quit to exit\n") #\n means "new line"
    gameVars.player_choice = input("Choose rock, paper, or scissors: \n")

    if gameVars.player_choice == "quit":
        print("You choose to quit")
        exit ()

    print("user chose: " + gameVars.player_choice)

    # this will be the AI choice -> a random pick from the choices array
    gameVars.computer_choice = gameVars.choices[randint(0, 2)]

    print("computer chose: " + gameVars.computer_choice)

    if gameVars.computer_choice == gameVars.player_choice:
        print ("tie")

    elif gameVars.computer_choice == "rock":
        if gameVars.player_choice == "scissors":
            print ("you lose!")
            #verbose way
            # player_lives = player_lives -1
            #simplified way
            gameVars.player_lives -= 1
        else:
            print ("you win")
            gameVars.computer_lives -=1

    elif gameVars.computer_choice == "paper":
        if gameVars.player_choice == "scissors":
            print ("you win!")
            gameVars.computer_lives -= 1
        else:
            print("you lose!")
            gameVars.player_lives -= 1

    elif gameVars.computer_choice == "scissors":
        if gameVars.player_choice == "paper":
         print("you lose!")
         gameVars.player_lives -= 1
        else:
         print("you win")
        gameVars.computer_lives -= 1
