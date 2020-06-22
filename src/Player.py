# -*- coding: utf-8 -*-
import sys

import numpy as np

from abc import ABC, abstractmethod 

from sklearn.neural_network import MLPClassifier

import keras
from keras.models import Sequential,Input,Model
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.layers.normalization import BatchNormalization
from keras.layers.advanced_activations import LeakyReLU
from sklearn.model_selection import train_test_split

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

        X = database.values[:,:-7]
        y = database.values[:,-7:]
        
        #Prepare data
        X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2)
        
        #Init model
        self.clf = Sequential()
             
        self.clf.add(Dense(42, activation='relu'))
        self.clf.add(Dense(21, activation='softmax'))
        self.clf.add(Dense(14, activation='relu'))
        #self.clf.add(Flatten())
        #self.clf.add(LeakyReLU(alpha=0.1))  
        #self.clf.add(Conv2D(32, kernel_size=(2, 2),activation='linear',input_shape=(1, 42),padding='same'))
        #self.clf.add(LeakyReLU(alpha=0.1))
        #self.clf.add(MaxPooling2D((2, 2),padding='same'))
        #self.clf.add(Conv2D(64, (3, 3), activation='linear',padding='same'))          
        
        self.clf.add(Dense(7, activation='softmax'))
        
        self.clf.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.Adam(),metrics=['accuracy'])
        
        #self.clf = MLPClassifier(hidden_layer_sizes=(30,15), activation='logistic', solver='lbfgs', max_iter=nb_iter)
        self.clf.fit(X_train, y_train, batch_size=32, epochs=50,verbose=1,validation_data=(X_valid, y_valid))
        self.clf.summary()
    
    def play(self) :
        board = np.reshape(np.array(self.game.array).ravel(), (1,42))
        #board *= self.game.currentPlayer
    
        prediction = self.clf.predict(board)
    
        decisions = np.argsort(prediction)[0][::-1]
        i=0
        while not self.game.play(decisions[i]) :
            i+=1