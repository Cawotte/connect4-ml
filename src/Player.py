# -*- coding: utf-8 -*-
import sys

import numpy as np

from abc import ABC, abstractmethod 

from sklearn.neural_network import MLPClassifier

class Player(ABC) :
    """
        An abstract class that represents a Connect4 Player
    
        Parameters
        ------------
        game, a Connect4 object
    """
    
    def __init__(self, game) :
        self.game = game
    
    @abstractmethod
    def play(self) :
        pass



class HumanPlayer(Player) :
    """
        a human player for connect4
        
        Parameters
        ------------
        game, a Connect4 object
    """
    
    def __init__(self, game) :
        Player.__init__(self, game)
    
    def play(self) :
        validMove = False
        while not validMove :
            choice = -1
            #while the column choice is not valid, scanf
            while (choice < 0 or choice >= self.game.width):
                inp = input("Please choose in which column to play (0 - {maxWidth}), or 'q' to exit:\n".format(maxWidth = self.game.width - 1))
                if (inp == "q"):
                    print("Exiting the game...")
                    sys.exit(0)
                try:
                    choice = int(inp)  
                except ValueError:
                    print("Invalid Value, please enter an integer")
                    
            validMove = self.game.play(choice)
            if not validMove :
                print("Can't play this move, the column is full!")


class MLPCPlayer(Player) :
    """
        a AI that uses an MLPClassifier to play connect4
        
        Parameters
        ------------
        game, a Connect4 object
        database, a pandas data object
    """
    
    def __init__(self, game, database, nb_iter=2000):
        Player.__init__(self,game)

        X_train = database.values[:,:-7]
        
        y_train = database.values[:,-7:]
        
        self.clf = MLPClassifier(hidden_layer_sizes=(30,15), activation='relu', solver='adam', max_iter=nb_iter)
        self.clf.fit(X_train, y_train)
    
    def play(self) :
        board = np.reshape(np.array(self.game.array).ravel(), (1,42))
        board*=self.game.currentPlayer
    
        prediction = self.clf.predict(board)
    
        decisions = np.argsort(prediction)[0][::-1]
        i=0
        while not self.game.play(decisions[i]) :
            i+=1