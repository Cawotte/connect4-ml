# -*- coding: utf-8 -*-

from sklearn.neural_network import MLPClassifier

import numpy as np
import pandas as pd

from Connect4 import Connect4

train_data = pd.read_csv('connect4-manual-database.csv', sep=';')

# print(train_data.values[-7])
X_train = train_data.values[:,:-7]

y_train = train_data.values[:,-7:]

clf = MLPClassifier()
clf.fit(X_train, y_train)

match = Connect4()


player = 1
while not match.gameHasEnded:
    board = np.reshape(np.array(match.array).ravel(), (1,42))
    board*=player
        
    prediction = clf.predict(board)
    print("Prediction array : %s" % prediction)

    col_to_play = prediction.argmax()
    print("Predicted move : %s" % col_to_play)
    validMove = match.play(col_to_play)
    if not validMove:
        print("Move is not valid, stopping...")
        break
    match.printBoard()
    player*=1

#%%%
    
# -*- coding: utf-8 -*-

from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

import numpy as np
import pandas as pd

from Connect4 import Connect4

train_data = pd.read_csv('D:/UQAC/apprentissage profond/Projet/connect4-ml/src/connect4-manual-database-double.csv', sep=';')

X_train = train_data.values[:,:-7]

y_train = train_data.values[:,-7:]

clf = MLPClassifier(hidden_layer_sizes=(30,15), activation='relu', solver='adam', max_iter=2000)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_train)

print(accuracy_score(y_train, y_pred))

match = Connect4()
player = 1
while not match.gameHasEnded:
    board = np.reshape(np.array(match.array).ravel(), (1,42))
    board*=player

    prediction = clf.predict(board)
    print("Prediction array : %s" % prediction)

    decisions = np.argsort(prediction)[0][::-1]
    print(decisions)
    i=0
    while not match.play(decisions[i]) :
        i+=1
    match.printBoard()
    player*=-1
    
#%% Convolution

from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten
from keras.models import Sequential

import numpy as np
import pandas as pd

from Connect4 import Connect4


#creation of the classifier
clf = Sequential()
input_img = (7, 6, 1)
clf.add(Conv2D(16, kernel_size=(5,5), activation='sigmoid', input_shape=input_img))
clf.add(MaxPooling2D(pool_size=(2, 2)))
clf.add(Flatten())
clf.add(Dense(50, activation='sigmoid'))
clf.add(Dense(7, activation='relu'))

clf.compile(optimizer='adam', loss='categorical_crossentropy')


#creation of the inputs
train_data = pd.read_csv('./connect4-manual-database-double.csv', sep=';')

X_train = train_data.values[:,:-7]
y_train = train_data.values[:,-7:]

print(X_train.shape)
X_train = np.reshape(X_train, (len(X_train), 7, 6, 1))
print(X_train.shape)

clf.fit(X_train, y_train,
                epochs=100,
                shuffle=True,
                validation_data=(X_train, y_train))


match = Connect4()
player = 1
while not match.gameHasEnded:
    board = np.reshape(np.array(match.array).ravel(), (1,7,6,1))
    board*=player
    
    prediction = clf.predict(board)
    print("Prediction array : %s" % prediction)

    col_to_play = prediction.argmax()
    print("Predicted move : %s" % col_to_play)
    decisions = np.argsort(prediction)[0][::-1]
    print(decisions)
    i=0
    while not match.play(decisions[i]) :
        i+=1
    match.printBoard()
    player*=-1
