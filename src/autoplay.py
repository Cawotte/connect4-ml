# -*- coding: utf-8 -*-
"""
This script plays several match of Connect4 with predetermined moves to test the result and verify
the Connect4 is working. Kind of a unit test.
"""

from Connect4 import Connect4

import random

#If verbose is True, display the final boards and results of the matchs.
verbose = True

#Each test to be performed, each element of the array has a movelist, and the expected winner
#  1 = Player 1, 
# -1 = Player 2,
#  0 = Draw

tests = [
    [[0, 0, 1, 1, 2, 2, 3], 1], #row
    [[0, 1, 0, 1, 0, 1, 0], 1], #column
    [[0, 1, 1, 2, 2, 3, 2, 3, 3, 1, 3], 1], #diagonal 1
    [[3, 2, 2, 1, 1, 0, 1, 0, 0, 1, 0], 1] #diagonal 2
    ]


match = Connect4()

#Prepare random movelist
movelist = []
for i in range(match.width):
    for j in range(match.height):
        movelist.append(i)
        
random.shuffle(movelist)
    
tests.append([movelist, 0])

successfulTestCount = 0
#for each move lists
for i in range(len(tests)):
    test = tests[i]
    
    movelist = test[0]
    expectedResult = test[1]
    
    #While there's still moves to perform and the game isn't over
    while (movelist and not match.gameHasEnded):
        choice = movelist[0]
        movelist.pop(0)
        
        validMove = match.play(choice)
        if (not validMove):
           print("Non-valid move! Moving to the next one...")
           
        
    #Verify the result of the game
    if (verbose):
        print()
        match.printBoard()
        match.printResults()
        match.drawBoard()
        print()
        
    if (match.winner == expectedResult):
        print("Test #", i, "successful!")
        successfulTestCount += 1
    else:
        print("Test #", i, "failed!")
    
    match.reset()
        
print("Test successful : ", successfulTestCount, "/", len(tests))
