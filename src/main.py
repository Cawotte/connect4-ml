# -*- coding: utf-8 -*-
"""

Main script

Can be used to play Connect4 with two human players using the console.
"""

from Connect4 import Connect4
from Player import HumanPlayer, MLPCPlayer
import random
import pandas as pd


#Initialize a game
match = Connect4()

train_data = pd.read_csv('./connect4-manual-database-double.csv', sep=';')

player1 = HumanPlayer(match)
player2 = MLPCPlayer(match, train_data)
players = [player1, player2]

tour = random.choice([0,1])
while (not match.gameHasEnded):
    players[tour].play()
    match.printBoard()
    tour = 1-tour
        
match.printResults()
