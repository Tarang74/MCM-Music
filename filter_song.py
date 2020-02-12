# Created by Tarang Janawalkar
# February 1, 2020

import itertools as it
import os
from collections import defaultdict

import numpy as np
import pandas as pd
from numpy import savetxt

numProgs = 0
numSongs = 0

chords = ["A", "Am", "A#", "A#m",
          "B", "Bm",
          "C", "Cm", "C#", "C#m",
          "D", "Dm", "D#", "D#m",
          "E", "Em",
          "F", "Fm", "F#", "F#m",
          "G", "Gm", "G#", "G#m"]  # list of all chords

# permutation of all chords (n^r)
progArray = np.asarray(list(it.product(chords, repeat=2)))

dict = {}  # empty dictionary for building pairs


def listToString(s):  # convert array values to string
    str = " "
    return (str.join(s))


sel = "major"  # input("major or minor (LC): ")  # input major or minor

for file1 in os.listdir(sel):  # repeat for all files in major or minor
    dir = sel + "/" + file1
    f = open(dir, "r+")  # open file
    songName = f.readline()
    songName = songName.strip("#")
    songName = songName.rstrip()

    lines = f.readlines()  # gather file contents
    f.close()  # close file

    a = '\t'.join([line.strip() for line in lines])  # remove multispaces
    # remove "No Chords" "C" may be recognised unintentionally
    a = a.replace('N.C.', '')
    a = ' '.join(a.split())  # split all words with space

    chordProg = [w for w in a.split() if w in chords]  # remove all but chords
    total = len(chordProg) - 1  # number of chord progressions

    answers = defaultdict(int)

    for i in range(progArray.shape[0]):
        s = progArray[i]
        newProgArray = listToString(s)
        for j in range(len(chordProg) - 1):
            if progArray[i][0] == chordProg[j] and progArray[i][1] == chordProg[j + 1]:
                answers[newProgArray] += 1
    for npA in sorted(answers.keys()):
        print(npA, answers[npA], file=open("temp.txt", "a"))

    raw = []
    with open('temp.txt', 'r') as file:
        for line in file:
            raw.append(line.split())

    tot = pd.DataFrame(raw, columns=['row', 'column', 'value'])
    tot = tot.rename_axis('ID').values
    dict[file1[:-4]] = tot

    os.remove("temp.txt")

    if sum(answers.values()) == total:
        numProgs = numProgs + total
        numSongs = numSongs + 1
    else:
        print("Total: " + str(sum(answers.values())) +
              " Does not match: " + str(total) + "\n")

stackedArray = np.empty(3)  # new blank array for combining results

for i in dict:  # loop to combine results
    stackedArray = np.vstack((stackedArray, dict[i]))
stackedArray = np.delete(stackedArray, 0, 0)

dict2 = {}  # new blank dictionary

for elem in stackedArray:
    key = tuple(elem[:-1])
    value = int(elem[-1])
    dict2[key] = dict2.get(key, 0) + value

finalArray = [[*key, value] for key, value in dict2.items()]
finalArray = np.array(finalArray)

# provide output to user
print("\n")
dash = '-' * 42
line = "|"
print(dash)
print("Found ", numProgs, " progressions from ", numSongs, " songs")
print(dash)

# save finalArray to txt file
np.savetxt('export.txt', finalArray, fmt='%s')
