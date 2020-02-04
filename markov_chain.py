import numpy as np
import itertools as it
import pandas as pd
import os
import sys
from collections import defaultdict
from io import StringIO
import random as rn

# Created by Leighton Swannell
# February 3, 2020

from filter_song import *

states = ["A", "Bm", "C#m", "D", "E", "F#m", "G#"] #All possible chords that can be combined
tName = [] #Transition names (eg. A-Bm)
tOccr = [] #Occurance matrix
tProb = [] #Probabilities matrix
tProbR = [] #Rounded matrix for viewer output
sumArry = []
xyMtrx = ["0", "1", "2", "3", "4", "5", "6"]

for i in states: #for every chord
    tI = [] #create temporary arrays
    tJ = []
    tK = []
    for j in states: #for every chord
        tI.append(j+"-"+i) #add combination of j and i to temp array
        tJ.append(0)
        tK.append(0.0)
    tName.append(tI) #add temp arrays to transition arrays
    tOccr.append(tJ)
    tProb.append(tK)
    tProbR.append(tK)

data = finalArray
print("\n")
for i in range(len(data)):
    if i == 0:
        print(dash)
        print('{:>12s}{:s}'.format("","Chord changes:"))
        print(dash)
        print('{:<12s}{:<13s}{:^8s}'.format("From", "To", "# of occurances"))
        print(dash)
    print("{:<12s}{:<22s}{:>6}".format(data[i][0], data[i][1], data[i][2]))

x = 0
y = 0
z = 0
for i in range(len(data)): #for every three value array
    for j in range(len(states)):
        if data[i][0] == states[j]: #where the first letter is a possible chord j
            x = j #matrix x coordinate
        if data[i][1] == states[j]: #where the second letter is a possible chord j
            y = j #matrix y coordinate
    z = data[i][2] #matrix value at coordinates
    tOccr[y].insert(x, z)

#create matrix T with values unrounded
f = 0
for i in range(len(tOccr)):
    for k in range(len(tOccr)):
        f = f + int(tOccr[i][k])
    sumArry.append(f)
    if f == 0:
        f = 1
    for j in range(len(tOccr)):
        tProb[i][j] = int(tOccr[i][j]) / f
    f = 0

#XY Position Matrix Output
print("\n")
for i in range(len(tOccr)):
    if i == 0:
        print(dash)
        print('{:>12s}{:s}'.format("","XY Position Matrix:"))
        print(dash)
        print('{:<6}{:<6s}{:<6s}{:<6s}{:<6s}{:<6s}{:<5s}{:<6s}'.format("",xyMtrx[0],xyMtrx[1],xyMtrx[2],xyMtrx[3],xyMtrx[4],xyMtrx[5],xyMtrx[6]))
        print(dash)
    print("{:<2s}{:<3s}{:>2}{:>6}{:>6}{:>6}{:>6}{:>6}{:>5}".format(xyMtrx[i], line, tOccr[i][0], tOccr[i][1], tOccr[i][2], tOccr[i][3], tOccr[i][4], tOccr[i][5], tOccr[i][6]))
#Sum Output
print(dash)
print(dash)
print("{:<4s}{:>2}{:>6}{:>6}{:>6}{:>6}{:>6}{:>5}".format("", sumArry[0], sumArry[1], sumArry[2], sumArry[3], sumArry[4], sumArry[5], sumArry[6]))

#round values of matrix T
for i in range(len(tOccr)):
    for j in range(len(tOccr)):
        tProbR[i][j] = round(tProb[i][j], 2)

print("\n")
for i in range(len(tProb)):
    if i == 0:
        print(dash)
        print('{:>12s}{:s}'.format("","Transition Matrix:"))
        print(dash)
        print('{:^4s}{:^8s}{:^4s}{:^7s}{:^6s}{:^6s}{:^7s}'.format(states[0],states[1],states[2],states[3],states[4],states[5],states[6]))
        print(dash)
    print("{:<6.2f}{:<6.2f}{:<6.2f}{:<6.2f}{:<6.2f}{:<6.2f}{:<5.2f}{:<2s}{:<4s}{:<2s}".format(tProb[i][0], tProb[i][1], tProb[i][2], tProb[i][3], tProb[i][4], tProb[i][5], tProb[i][6], line, states[i], line))
print("\n")
