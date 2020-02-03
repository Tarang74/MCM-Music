import numpy as np
import itertools as it
import pandas as pd
import os
from collections import defaultdict

chords = ["A", "Am", "A#", "A#m",
                "B", "Bm",
                "C", "Cm", "C#", "C#m",
                "D", "Dm", "D#", "D#m",
                "E", "Em",
                "F", "Fm", "F#", "F#m",
                "G", "Gm", "G#", "G#m"]

progArray = np.asarray(list(it.product(chords, repeat=2)))

dict = {}

def listToString(s):
    str = " "
    return (str.join(s))

for file1 in os.listdir("major"):
    dir = "major/" + file1
    f = open(dir, "r+")
    print("File: " + file1 + " - Name: " + f.readline())

    lines = f.readlines()
    a = '\t'.join([line.strip() for line in lines])
    a = a.replace('N.C.', '')
    a = ' '.join(a.split())
    f.close()

    chordProg = [w for w in a.split() if w in chords]
    total = len(chordProg) - 1
    #print(str(len(chordProg)) + " chords: " + str(total) + " chord progressions\n")

    answers = defaultdict(int)

    for i in range(progArray.shape[0]):
        s = progArray[i]
        newProgArray = listToString(s)
        for j in range(len(chordProg) - 1):
            if progArray[i][0] == chordProg[j] and progArray[i][1] == chordProg[j + 1]:
                answers[newProgArray] += 1
    for npA in sorted(answers.keys()):
        print(npA, answers[npA], file=open("output.txt", "a"))

    raw = []
    with open('output.txt', 'r') as file:
        for line in file:
            raw.append(line.split())

    tot = pd.DataFrame(raw, columns=['row', 'column', 'value'])
    tot = tot.rename_axis('ID').values
    print(tot)
    dict[file1[:-4]] = tot

    os.remove("output.txt")

    if sum(answers.values()) == total:
        print("Total: " + str(sum(answers.values())) + "\n")
    else:
        print("Total: " + str(sum(answers.values())) + " Does not match: " + str(total) + "\n")

final = np.empty(3)

for i in dict:
    final = np.vstack((final, dict[i]))
final = np.delete(final, 0, 0)
print(final)
