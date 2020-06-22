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

#Initiliaze database
mainDbName = database_name + ".csv"
mirrorDbName = database_name + "-mirror.csv"

#We are gonna use tehe copy of the registered database, and mirror it
dbMirror = copyfile(mainDbName, mirrorDbName)
#mirror it
mirrorDouble(mirrorDbName) 

#Use the mirrored data
train_data = pd.read_csv('./' + mirrorDbName, sep=';')


#Initialize a game
match = Connect4(register=True)


player1 = HumanPlayer(match)
player2 = MLPCPlayer(match, train_data)
players = [player1, player2]

gamesLeft = 15

while gamesLeft > 0:
    
    print("Starting a new game! #", gamesLeft)
    
    tour = 0
    while (not match.gameHasEnded):
        players[tour].play()
        match.printBoard()
        tour = 1-tour
            
    match.printResults()
    match.reset()
    
    gamesLeft -= 1
