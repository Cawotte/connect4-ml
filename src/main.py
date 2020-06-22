# -*- coding: utf-8 -*-
"""

Main script

Can be used to play Connect4 with two human players using the console.
"""

from Connect4 import Connect4
from Player import HumanPlayer, MLPCPlayer
import random
import pandas as pd
from preprocessing import mirrorDouble

from shutil import copyfile

database_name = "connect4-manual-database"

# ----- Initiliaze databases -----
mainDbName = database_name + ".csv"
mirrorDbName = database_name + "-mirror.csv"

#Copy the main database,
dbMirror = copyfile(mainDbName, mirrorDbName)
mirrorDouble(mirrorDbName)  # then mirror it

train_data = pd.read_csv('./' + mirrorDbName, sep=';') #Use the mirrored data
train_data.drop_duplicates()


# ------ Initialize a game -----
match = Connect4(register=True)


player1 = HumanPlayer(match)
player2 = MLPCPlayer(match, train_data)
players = [player1, player2]

gamesLeft = 15

while gamesLeft > 0:
    
    print("Starting a new game! #", gamesLeft)
    
    tour = random.choice([0,1])
    while (not match.gameHasEnded):
        
        #If it's the player's turn, register the move.
        match.register = (tour == 0)
        
        players[tour].play()
        match.printBoard()
        tour = 1-tour
            
    match.printResults()
    match.reset()
    
    gamesLeft -= 1
