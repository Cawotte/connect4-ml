# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 15:36:00 2020

@author: Cawotte
"""

import numpy as np

class Connect4(object):
    """
        Object to represent and play matches of Connect4.
        
        Parameters
        ------------
        width, height : Size of the board.
        
        Other Info
        ------------
        
        The coordinates are [i, j], i is the column number, and j the row number has such :
            
            5| -  -  -  -  -  -  - 
            4| -  -  -  -  -  -  - 
            3| -  -  -  X  -  -  - 
            2| -  0  X  X  -  -  - 
            1| -  X  X  0  -  -  - 
            0| X  0  0  0  -  -  - 
             ----------------------
               0  1  2  3  4  5  6
               
        (2, 2) is X
        (2, 0) is 0
        (0, 2) is empty
        """
    
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
        
    def reset(self):
        
        """
        Reset the state of the game to an empty board and new game.
        """
        
        #empty the array
        self.array = np.zeros(shape=(self.width, self.height))
        
        self.currentPlayer = 1
        self.winner = 0
        self.gameHasEnded = False
        self.plyCount = 0
        
    def play(self, column):
        """
        Play a move.
        
        Parameters
        ------------
        column : The column index at which to play the move

        Returns
        -----------
        boolean : True if the move is performed, False if the column is full
        """
        
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
        
        """
        Print the board state in the console.
        """
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
            
    def printResults(self):
        """
        Print the result of the match in the console.
        """
        print("---- RESULTS -----")
        if (self.gameHasEnded):
            winnerStr = ""
            if (self.winner == 1):
                print("Player 1 has won the match!")
            elif (self.winner == -1):
                print("Player 2 has won the match!")
            elif (self.winner == 0):
                print("No winner, this is draw.")
            else: #impossible scenario, normally
                print("ERROR, impossible scenario")
        else:
            print("The game is still ongoing, there's no winner.")
            
                    
    #Check if the chip at that location is part of a winning row
    def _isWinningPlay(self, column, row):
        """
        Verify if the given position is part of a winning line. Verified after each move.
        
        Parameters
        ------------
        column, row : indexes of the move to verify

        Returns
        -----------
        boolean : True if the move is part of a line and winning, False otherwise.
        """
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
        
    
    
    
    