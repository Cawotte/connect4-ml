# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 16:11:27 2020

@author: Cawotte
"""

from Connect4 import Connect4


def chooseMoveset(choice):
    if (choice == 0):
        return []
    if (choice == 1):
        #row
        return [0, 0, 1, 1, 2, 2, 3, 3]
    if (choice == 2):
        #column
        return [0, 1, 0, 1, 0, 1, 0, 1]
    if (choice == 3):
        #diagonal 1
        return [0, 1, 1, 2, 2, 3, 2, 3, 3, 1, 3]
    if (choice == 4):
        #diagonal 2
        return [3, 2, 2, 1, 1, 0, 1, 0, 0, 1, 0]

    return []

#Initialize a game
match = Connect4()

#movesets for case tests
moveset = chooseMoveset(4)

while (not match.gameHasEnded):
    
    #If there's predefined moves left
    if moveset:
        choice = moveset[0]
        moveset.pop(0)
        print("") #linebreak
    else:
        print("Please choose in which column to play")
        
        choice = -1
        #while the column choice is not valid, scanf
        while (choice < 0 or choice >= match.width):
            try:
                choice = int(input())  
            except ValueError:
                print("Invalid Value : Abort Game")
                match.gameHasEnded = True
                break
            
    validMove = match.play(choice)
    if (validMove):
        match.printBoard()
        
print("---- GAME HAS ENDED ----")
print("Player ", match.winner, " has won the game!")

