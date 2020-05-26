# Created by Tarang Janawalkar
# February 1, 2020

import itertools as it
import os
from collections import defaultdict

import numpy as np
import pandas as pd
from numpy import savetxt

if (os.path.exists("output") == False):
    os.makedirs("output")

chords = [
    "A#m", "A#", "Am", "A", "Bm", "B", "C#m", "C#", "Cm", "C", "D#m", "D#",
    "Dm", "D", "Em", "E", "F#m", "F#", "Fm", "F", "G#m", "G#", "Gm", "G"
]  # list of all chords    

progArray = np.asarray(list(it.product(chords, repeat=2)))
# permutation of all chords (n^r)

class FilterSongs:


numProgs = 0
numSongs = 0





dict = {}  # empty dictionary for building pairs


def listToString(s):  # convert array values to string
    str = " "
    return str.join(s)


sel = input("Select folder: ")  # input major or minor

for file1 in os.listdir(sel):  # repeat for all files in major or minor
    dir = sel + "/" + file1

    lines = ""
    with open(dir, "r+") as f:
        count = 0
        for line in f:
            count += 1
            if count % 2 == 0:
                lines = lines + line

    f.close()  # close file

    a = lines
    a = a.replace("N.C.", "")
    a = a.replace("*", "")
    a = " ".join(a.split())

    chordProg = [w for w in a.split() if w in chords]  # remove all but chords
    total = len(chordProg) - 1  # number of chord progressions

    answers = defaultdict(int)

    for i in range(0, progArray.shape[0]):
        s = progArray[i]
        newProgArray = listToString(s)
        for j in range(len(chordProg) - 1):
            if progArray[i][0] == chordProg[j] and progArray[i][
                    1] == chordProg[j + 1]:
                answers[newProgArray] += 1
    for npA in sorted(answers.keys()):
        print(npA, answers[npA], file=open("temp.txt", "a"))

    raw = []
    with open("temp.txt", "r") as file:
        for line in file:
            raw.append(line.split())

    tot = pd.DataFrame(raw, columns=["row", "column", "value"])
    tot = tot.rename_axis("ID").values
    dict[file1[:-4]] = tot

    os.remove("temp.txt")

    if sum(answers.values()) == total:
        numProgs = numProgs + total
        numSongs = numSongs + 1
    else:
        print("Total: " + str(sum(answers.values())) + " Does not match: " +
              str(total) + "\n")

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
dash = "-" * 42
line = "|"
print(dash)
print(" Found ", numProgs, " progressions from ", numSongs, " songs")
print(dash)

if (os.path.exists("output/TransitionList.txt") == True):
    os.remove("output/TransitionList.txt")  # delete if already exists
    np.savetxt("output/TransitionList.txt", finalArray, fmt="%s")
else:
    np.savetxt("output/TransitionList.txt", finalArray,
               fmt="%s")  # save finalArray to txt file

states = np.unique(finalArray)
delete = np.array([], dtype=np.int)

for i in range(len(states)):
    try:
        a = int(states[i]) + 1
    except ValueError:
        continue
    else:
        delete = np.append(delete, i)

states = np.delete(states, delete)
print("Chords Used: ")
print(states)
