# -*- coding: utf-8 -*-
"""

Main script

Can be used to play Connect4 with two human players using the console.
"""

from Connect4 import Connect4

import sys #To exit main

#Initialize a game
match = Connect4(register=True)

while (not match.gameHasEnded):
    
    choice = -1
    #while the column choice is not valid, scanf
    while (choice < 0 or choice >= match.width):
        inp = input("Please choose in which column to play (0 - {maxWidth}), or 'q' to exit:\n".format(maxWidth = match.width - 1))
        if (inp == "q"):
            print("Exiting the game...")
            sys.exit(0)
        try:
            choice = int(inp)  
        except ValueError:
            print("Invalid Value, please enter an integer")
            
    validMove = match.play(choice)
    if (validMove):
        match.printBoard()
    else:
        print("Can't play this move, the column is full!")
        
match.printResults()
del(match)
