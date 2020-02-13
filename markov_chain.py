# Created by Leighton Swannell
# February 3, 2020
# Modified for all chords by Tarang Janawalkar
# February 5, 2020

from filter_song import *

states = [
    "A", "Am", "A#", "A#m", "B", "Bm", "C", "Cm", "C#", "C#m", "D", "Dm", "D#",
    "D#m", "E", "Em", "F", "Fm", "F#", "F#m", "G", "Gm", "G#", "G#m"
]  # All possible chords that can be combined
tName = []  # Transition names (eg. A-Bm)
tOccr = []  # Occurance matrix
tProb = []  # Probabilities matrix
tProbR = []  # Rounded Probabilities matrix
sumArry = []
sumTcol = []
xyMtrx = [
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13",
    "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"
]
dash2 = "-" * 175

for i in states:  # for every chord
    tI = []  # create temporary arrays
    tJ = []
    tK = []
    for j in states:  # for every chord
        tI.append(j + "-" + i)  # add combination of j and i to temp array
        tJ.append(0)
        tK.append(0.0)
    tName.append(tI)  # add temp arrays to transition arrays
    tOccr.append(tJ)
    tProb.append(tK)

data = finalArray
for i in range(len(data)):
    if i == 0:
        print(dash)
        print('{:>14s}{:s}'.format("", "Chord changes:"))
        print(dash)
        print('{:<12s}{:<13s}{:^8s}'.format("From", "To", "# of occurances"))
        print(dash)
    print("{:<12s}{:<22s}{:>6}".format(data[i][0], data[i][1], data[i][2]))

x = 0
y = 0
z = 0
for i in range(len(data)):  # for every three value array
    for j in range(len(states)):
        if data[i][0] == states[
                j]:  # where the first letter is a possible chord j
            x = j  # matrix x coordinate
        if data[i][1] == states[
                j]:  # where the second letter is a possible chord j
            y = j  # matrix y coordinate
    z = data[i][2]  # matrix value at coordinates
    tOccr[y].insert(x, z)

# create matrix T with values unrounded
f = 0
for i in range(len(tOccr)):
    for k in range(len(tOccr)):
        f = f + int(tOccr[k][i])
    sumArry.append(f)
    if f == 0:
        f = 1
    for j in range(len(tOccr)):
        tProb[j][i] = int(tOccr[j][i]) / f
    f = 0

# XY Position Matrix Output
print("\n")
for i in range(len(tOccr)):
    if i == 0:
        print(dash2)
        print('{:>81s}{:s}'.format("", "Chord Matrix:"))
        print(dash2)
        print(
            '{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}'
            .format(states[0], states[1], states[2], states[3], states[4],
                    states[5], states[6], states[7], states[8], states[9],
                    states[10], states[11], states[12], states[13], states[14],
                    states[15], states[16], states[17], states[18], states[19],
                    states[20], states[21], states[22], states[23]))
        print(dash2)
    print(
        "{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<2s}{:<4s}{:<2s}"
        .format(tOccr[i][0], tOccr[i][1], tOccr[i][2], tOccr[i][3],
                tOccr[i][4], tOccr[i][5], tOccr[i][6], tOccr[i][7],
                tOccr[i][8], tOccr[i][9], tOccr[i][10], tOccr[i][11],
                tOccr[i][12], tOccr[i][13], tOccr[i][14], tOccr[i][15],
                tOccr[i][16], tOccr[i][17], tOccr[i][18], tOccr[i][19],
                tOccr[i][20], tOccr[i][21], tOccr[i][22], tOccr[i][23], line,
                states[i], line))
# Sum Output
print(dash2)
print(
    "{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<2s}{:<4s}{:<2s}"
    .format(sumArry[0], sumArry[1], sumArry[2], sumArry[3], sumArry[4],
            sumArry[5], sumArry[6], sumArry[7], sumArry[8], sumArry[9],
            sumArry[10], sumArry[11], sumArry[12], sumArry[13], sumArry[14],
            sumArry[15], sumArry[16], sumArry[17], sumArry[18], sumArry[19],
            sumArry[20], sumArry[21], sumArry[22], sumArry[23], line, "Tot",
            line))

print("\n")
for i in range(len(tProb)):
    if i == 0:
        print(dash2)
        print('{:>78s}{:s}'.format("", "Transition Matrix:"))
        print(dash2)
        print(
            '{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}'
            .format(states[0], states[1], states[2], states[3], states[4],
                    states[5], states[6], states[7], states[8], states[9],
                    states[10], states[11], states[12], states[13], states[14],
                    states[15], states[16], states[17], states[18], states[19],
                    states[20], states[21], states[22], states[23]))
        print(dash2)
    print(
        "{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}{:<2s}{:<4s}{:<2s}"
        .format(round(tProb[i][0], 4), round(tProb[i][1], 4),
                round(tProb[i][2], 4), round(tProb[i][3], 4),
                round(tProb[i][4], 4), round(tProb[i][5], 4),
                round(tProb[i][6], 4), round(tProb[i][7], 4),
                round(tProb[i][8], 4), round(tProb[i][9], 4),
                round(tProb[i][10], 4), round(tProb[i][11], 4),
                round(tProb[i][12], 4), round(tProb[i][13], 4),
                round(tProb[i][14], 4), round(tProb[i][15], 4),
                round(tProb[i][16], 4), round(tProb[i][17], 4),
                round(tProb[i][18], 4), round(tProb[i][19], 4),
                round(tProb[i][20], 4), round(tProb[i][21], 4),
                round(tProb[i][22], 4), round(tProb[i][23], 4), line,
                states[i], line))
print(dash2)
print("\n")

markovMatrix = np.asarray([tProb])
# Sum of columns in Markov Matrix
sum = np.squeeze(np.sum(a=markovMatrix, axis=1, dtype=float))
dash3 = "-" * 73
print(dash3)
print("{:<25}{:s}".format("", "Sum of matrix columns:"))
print(dash3)
print(sum)
print(dash3)
print("\n")

start = "A"  # input("Enter starting note: ")  # Starting note
startMatrix = np.zeros((24, 1))  # All other notes have 0 probability

currentProbability = int
for i in range(len(states)):  # Set 1, to row of startMatrix
    if start == states[i]:
        startMatrix[i][0] = 1
        currentProbability = i

dash4 = "-" * 67
print(dash4)
print("{:<20}{:s}".format("", "Start Probability Matrix:"))
print(dash4)
print(np.squeeze(markovMatrix[:, currentProbability]))
print(dash4)
print("\n")
multPower = int(input("Number of Transition events: "))
print("\n")
print(dash4)
print("End Probability Matrix:")
print(dash4)
endMatrix = np.squeeze(
    np.dot(np.linalg.matrix_power(markovMatrix, i), startMatrix))
print(endMatrix)
print(dash4)
print("\n")

print("Chord Progression for " + str(multPower) + " transitions:")

statesIndex = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23
]
chordGeneration = np.zeros(multPower, dtype=int)

for i in range(1, multPower):
    prob = np.dot(np.linalg.matrix_power(markovMatrix, i), startMatrix)
    prob = np.squeeze(prob).tolist()

    chordGeneration[i] = np.random.choice(statesIndex, p=prob)
    # print(prob)  # Each column matrix probability

for i in range(len(chordGeneration)):
    print(chordGeneration)

finalChords = [""] * multPower

for i in range(len(chordGeneration)):
    a = chordGeneration[i]
    finalChords[i] = states[a]

print(finalChords)
