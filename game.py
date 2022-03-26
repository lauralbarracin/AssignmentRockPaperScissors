from random import randint
from tkinter import N
from gameComponents import gameVars, winLose
from gameComponents import gameOptions
 
while gameVars.player_choice is False: 
    gameOptions.gameOptions()

    if gameVars.player_lives == 0:
        winLose.winorlose("lose")
        
    if gameVars.computer_lives == 0:
        winLose.winorlose("won")
       
    print ("Player lives:", gameVars.player_lives)
    print ("Computer lives", gameVars.computer_lives)

gameVars.player_choice = False
