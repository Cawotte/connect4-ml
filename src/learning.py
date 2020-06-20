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



while not match.gameHasEnded:
    board = np.reshape(np.array(match.array).ravel(), (1,42))

    prediction = clf.predict(board)
    print("Prediction array : %s" % prediction)

    col_to_play = prediction.argmax()
    print("Predicted move : %s" % col_to_play)
    validMove = match.play(col_to_play)
    if not validMove:
        print("Move is not valid, stopping...")
        break
    match.printBoard()

#%%%
    
# -*- coding: utf-8 -*-

from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

import numpy as np
import pandas as pd

train_data = pd.read_csv('./connect4-manual-database-double.csv', sep=';')

#print(train_data.values[0])
X_train = train_data.values[:,:-7]

y_train = train_data.values[:,-7:]

clf = MLPClassifier(hidden_layer_sizes=(30,15), activation='relu', solver='adam', max_iter=2000)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_train)

print(accuracy_score(y_train, y_pred))

match = Connect4()

while not match.gameHasEnded:
    board = np.reshape(np.array(match.array).ravel(), (1,42))

    prediction = clf.predict(board)
    print("Prediction array : %s" % prediction)

    col_to_play = prediction.argmax()
    print("Predicted move : %s" % col_to_play)
    validMove = match.play(col_to_play)
    if not validMove:
        print("Move is not valid, stopping...")
        break
    match.printBoard()