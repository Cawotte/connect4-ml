# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 15:36:00 2020

@author: Cawotte
"""

import numpy as np

class Connect4(object):
    def __init__(self, width = 7, height = 6):
        
        #gameboard
        self.width = width
        self.height = height
        self.array = np.zeros(shape=(width, height))
        
        #current game stats
        self.currentPlayer = 1
        self.winner = 0
        self.gameHasEnded = False
        
        self.plyCount = 0
        
    def resetGame(self):
        #empty the array
        self.array = np.zeros(shape=(self.width, self.eight))
        
        self.currentPlayer = 1
        self.winner = 0
        self.gameHasEnded = False
        self.plyCount = 0
        
    def play(self, column):
        
        for i in range(self.height):
            
            #If the cell is empty, place a chip
            if (self.array[column, i] == 0):
                self.array[column, i] = self.currentPlayer
                #change current player
                self.currentPlayer *= -1
                self.plyCount += 1
                #check if move is winning
                self._isWinningPlay(column, i)
                return True
        
        #The column is full, can't play here
        
        return False
    
    def printBoard(self):
        
        for j in range(self.height):
            line = ""
            for i in range(self.width):
                value = self.array[i, self.height - j - 1]
                if (value == 0):
                    line += " - "
                elif (value == 1):
                    line += " X "
                elif (value == -1):
                    line += " 0 "
            print(line)
                    
    #Check if the chip at that location is part of a winning row
    def _isWinningPlay(self, column, row):
        
        value = self.array[column, row]
        
        #if empty, it's not winning
        if (value == 0):
            return False
        
        consecutive = 0
        
        #check the column
        for j in range(self.height):
            if (self.array[column, j] == value):
                consecutive += 1
            else:
                consecutive = 0
                
            if (consecutive >= 4):
                self.gameHasEnded = True
                self.winner = value
                return True
            
        #check the row
        consecutive = 0
        for i in range(self.width):
            if (self.array[i, row] == value):
                consecutive += 1
            else:
                consecutive = 0
                
            if (consecutive >= 4):
                self.gameHasEnded = True
                self.winner = value
                return True
        
        #Check the diagonals
        
        consecutive = 0
        #to know where the diagonal begins and end, we need to know the start and end of the diagonal
        minV = min(column, row)
        a = column - minV
        b = row - minV
        
        while a < self.width and b < column:
            if (self.array[a, b] == value):
                consecutive += 1
            else:
                consecutive = 0
                
            if (consecutive >= 4):
                self.gameHasEnded = True
                self.winner = value
                return True
            
            #increment pos
            a += 1
            b += 1
            
        #The other diagonal
        #a bit clunky, to improve?
        a, b = column, row
        #decrement value until reaching end of diagonal
        while (a > 0 and b < self.height - 1):
            a -= 1
            b += 1
            
        #We are now at the top left of the diagonal
        while (a < self.width and b > 0):
            if (self.array[a, b] == value):
                consecutive += 1
            else:
                consecutive = 0
                
            if (consecutive >= 4):
                self.gameHasEnded = True
                self.winner = value
                return True
            
            #increment pos
            a += 1
            b -= 1
            
        #Not line of 4 found nowhere, no winner
        return False
        
    
    
    
    