# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 14:53:39 2020

@author: nbarl
"""

import csv

def mirrorDouble(fileName) :
    with open(fileName, 'r+', newline='') as file:
        dataReader = csv.reader(file, delimiter=';')
        newData = []
        for row in dataReader :
            newLine = createMirror(row)
            newData.append(newLine)
        
        dataWriter = csv.writer(file, delimiter=';')
        for row in newData[1:] :
            dataWriter.writerow(row)

def createMirror(l) :
    newL = []
    width = 7
    height = 6
    for i in range(width) :
        for j in range(height) :
            newL.append(l[height*(width-i-1) + j])
    shift = width*height
    for i in range(width) :
        newL.append(l[width-i-1+shift])
    return newL