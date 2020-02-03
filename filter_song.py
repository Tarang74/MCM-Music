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
                "G", "Gm", "G#", "G#m"] #list of all chords

progArray = np.asarray(list(it.product(chords, repeat=2))) #permutation of all chords (n^r)

dict = {} #empty dictionary for building pairs

def listToString(s): #convert array values to string
    str = " "
    return (str.join(s))
sel = input("major or minor (LC): ") #input major or minor

for file1 in os.listdir(sel):  #repeat for all files in major or minor
    dir = sel + "/" + file1
    f = open(dir, "r+") #open file
    print("File: " + file1 + " - Name: " + f.readline()) #file/song name

    lines = f.readlines() #gather file contents
    f.close() #close file

    a = '\t'.join([line.strip() for line in lines]) #remove multispaces
    a = a.replace('N.C.', '') #remove "No Chords" "C" may be recognised unintentionally
    a = ' '.join(a.split()) #split all words with space

    chordProg = [w for w in a.split() if w in chords] #remove all but chords
    total = len(chordProg) - 1 #number of chord progressions
    #print(str(len(chordProg)) + " chords: " + str(total) + " chord progressions\n")

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
    print(tot)
    dict[file1[:-4]] = tot

    os.remove("temp.txt")

    if sum(answers.values()) == total:
        print("Total: " + str(sum(answers.values())) + "\n")
    else:
        print("Total: " + str(sum(answers.values())) + " Does not match: " + str(total) + "\n")

stackedArray = np.empty(3) #new blank array for combining results

for i in dict: #loop to combine results
    stackedArray = np.vstack((stackedArray, dict[i]))
stackedArray = np.delete(stackedArray, 0, 0)

dict2 = {} #new blank dictionary

for elem in stackedArray:
    key = tuple(elem[:-1])
    value = int(elem[-1])
    dict2[key] = dict2.get(key,0) + value

finalArray = [[*key, value] for key, value in dict2.items()]
print(finalArray)