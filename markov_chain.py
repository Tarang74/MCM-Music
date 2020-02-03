import numpy as np
import itertools as it
import pandas as pd
import os
import sys
from collections import defaultdict
from io import StringIO
import random as rn
from filter_song import finalArray

states = ["A", "Bm", "C#m", "D", "E", "F#m", "G#"] #All possible chords that can be combined
tName = [] #Transition names (eg. A-Bm)
tOccr = [] #Occurance matrix
tProb = [] #Probabilities matrix
total = 68 #from filter_song.py

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

# raw = []
# with open('output.txt', 'r') as file: #open output.txt file and create array of data
#     for line in file:
#         raw.append(line.split())
# data = pd.DataFrame(raw,columns = ['row','column','value'])
# data = data.rename_axis('ID').values
data = finalArray
print("\n")
print("Values from output.txt file:")
for i in data:
    print(i)

x = 0
y = 0
z = 0
print("\n")
print("XY coordinates and values from output.txt file:")
for i in range(len(data)): #for every three value array
    for j in range(len(states)):
        if data[i][0] == states[j]: #where the first letter is a possible chord j
            x = j #matrix x coordinate
        if data[i][1] == states[j]: #where the second letter is a possible chord j
            y = j #matrix y coordinate
    z = data[i][2] #matrix value at coordinates
    print(x, y, z)
    tOccr[y].insert(x, z)

#create matrix T with values unrounded
for i in range(len(tOccr)):
    for j in range(len(tOccr)):
        tProb[i][j] = int(tOccr[i][j]) / total

print("\n")
print("Transition combinations (From-To):")
for i in tName:
    print(i)
print("\n")
print("Occurance of transitions:")
for i in tOccr:
    print(i)
print("\n")
print("Probability matrix of transitions (not rounded):")
for i in tProb:
    print(i)

#round values of matrix T
for i in range(len(tOccr)):
    for j in range(len(tOccr)):
        tProb[i][j] = round(tProb[i][j], 2)

print("\n")
print("Probability matrix of transitions (rounded):")
for i in tProb:
    print(i)
print("\n")

#sum of columns in tOccr:
f = 0
for i in range(len(tOccr)):
    for j in range(len(tOccr)):
        f = f + int(tOccr[j][i])
    print(f)
    f = 0