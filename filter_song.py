import numpy as np
import itertools as it
import pandas as pd
import os
import sys

from collections import defaultdict
from io import StringIO

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Invalid number of arguments:')
        print('Example usage: python3 filter_song.py <in.txt> <out.txt>')

f = open(sys.argv[1], "r+")
print("Name of song: ", f.readline())

lines = f.readlines()
a = '\t'.join([line.strip() for line in lines])
a = a.replace('N.C.', '')
a = ' '.join(a.split())

f.close()
os.remove("output.txt")

chords = ["A", "Am", "A#", "A#m",
          "B", "Bm",
          "C", "Cm", "C#", "C#m",
          "D", "Dm", "D#", "D#m",
          "E", "Em",
          "F", "Fm", "F#", "F#m",
          "G", "Gm", "G#", "G#m"]

progArray = np.asarray(list(it.product(chords, repeat=2)))

chordProg = [w for w in a.split() if w in chords]

total = len(chordProg) - 1

print(str(len(chordProg)) + " chords: " + str(total) + " chord progressions\n")

def listToString(s):
    str = " "
    return (str.join(s))

answers = defaultdict(int)

for i in range(progArray.shape[0]):
    s = progArray[i]
    newProgArray = listToString(s)
    for j in range(len(chordProg) - 1):
        if progArray[i][0] == chordProg[j] and progArray[i][1] == chordProg[j + 1]:
            answers[newProgArray] += 1
for npA in sorted(answers.keys()):
    print(npA, answers[npA], file=open(sys.argv[2], "a"))

raw = []
with open('output.txt', 'r') as file:
    for line in file:
        raw.append(line.split())
data = pd.DataFrame(raw,columns = ['row','column','value'])
data = data.rename_axis('ID').values
print(data)
os.remove("output.txt")

if sum(answers.values()) == total:
    print("Total was achieved - " + str(sum(answers.values())))
else:
    print("Total was not achieved - " + str(sum(answers.values())))

#Markov Chain Matrix