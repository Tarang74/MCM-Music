# Created by Leighton Swannell
# February 3, 2020
# Modified for all chords by Tarang Janawalkar
# February 5, 2020

import math
import matplotlib as mpl
import matplotlib.pyplot as plot
from filter_song import *

tName = []  # Transition names (eg. A-Bm)
tOccr = []  # Occurance matrix
tProb = []  # Probabilities matrix
tProbR = []  # Rounded Probabilities matrix
sumArry = []
dash2 = "-" * 7 * (len(states) + 1)

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
printtext = math.floor((3.5 * len(states)) - 3.5)

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
        print(" " * printtext, "Chord Matrix:")
        print(dash2)
        m = len(states)
        a = "{:<7}" * m
        b = "'" + a + "'.format("
        c = ""
        d = ")"
        for j in range(len(states)):
            c = c + "states[" + str(j) + "], "
        out = b + c + d
        print(eval(out))
        print(dash2)

    m = len(states)
    a = "{:<7}" * m + "{:<2s}{:<4s}{:<2s}"
    b = "'" + a + "'.format("
    c = ""
    d = " line, states[i], line)"
    for j in range(len(states)):
        c = c + "tOccr[" + "i][" + str(j) + "], "
    out = b + c + d
    print(eval(out))

# Sum Output
print(dash2)

m = len(states)
a = "{:<7}" * m + "{:<2s}{:<4s}{:<2s}"
b = "'" + a + "'.format("
c = ""
d = " line, 'Tot', line)"
for j in range(len(states)):
    c = c + "sumArry[" + str(j) + "], "
out = b + c + d
print(eval(out))
printtext1 = math.floor((3.5 * len(states)) - 5.5)
print("\n")

for i in range(len(tProb)):
    if i == 0:
        print(dash2)
        print(" " * printtext1, "Transition Matrix:")
        print(dash2)
        m = len(states)
        a = "{:<7}" * m
        b = "'" + a + "'.format("
        c = ""
        d = ")"
        for j in range(len(states)):
            c = c + "states[" + str(j) + "], "
        out = b + c + d
        print(eval(out))
        print(dash2)

    m = len(states)
    a = "{:<7}" * m + "{:<2s}{:<4s}{:<2s}"
    b = "'" + a + "'.format("
    c = ""
    d = " line, states[i], line)"
    for j in range(len(states)):
        c = c + "round(tProb[" + "i][" + str(j) + "], 4), "
    out = b + c + d
    print(eval(out))

print(dash2)
print("\n")

markovMatrix = np.asarray([tProb])
# Sum of columns in Markov Matrix
sum = np.squeeze(np.sum(a=markovMatrix, axis=1, dtype=float))
dash3 = "-" * 73
# print(dash3)
# print("{:<25}{:s}".format("", "Sum of matrix columns:"))
# print(dash3)
# print(sum)
# print(dash3)
# print("\n")

start = "A"  # input("Enter starting note: ")  # Starting note
startMatrix = np.zeros((len(states), 1))  # All other notes have 0 probability

for i in range(len(states)):  # Set 1, to row of startMatrix
    if start == states[i]:
        startMatrix[i][0] = 1

dash4 = "-" * 67
print(dash4)
print("{:<20}{:s}".format("", "Start Probability Matrix:"))
print(dash4)
print(np.squeeze(np.dot(markovMatrix, startMatrix)))
print(dash4)
print("\n")
multPower = int(input("Number of Transition events: ")) + 1
print("\n")
print(dash4)
print("End Probability Matrix:")
print(dash4)
endMatrix = np.squeeze(
    np.dot(np.linalg.matrix_power(markovMatrix, i), startMatrix))
print(endMatrix)
print(dash4)
print("\n")

statesIndex = np.arange(0, len(states))
chordGeneration = np.zeros(multPower, dtype=int)

for i in range(0, multPower):
    prob = np.dot(np.linalg.matrix_power(markovMatrix, i), startMatrix)
    prob = np.squeeze(prob).tolist()

    chordGeneration[i] = np.random.choice(statesIndex, p=prob)
    print("It no: ", i)
    print(np.round(prob, 4))  # Each column matrix probability
    print("\n")

print("Chord Progression for " + str(multPower - 1) + " transitions:")
print("\n")

print(chordGeneration)
print("\n")
finalChords = [""] * multPower

for i in range(len(chordGeneration)):
    a = chordGeneration[i]
    finalChords[i] = states[a]

print(finalChords)
print("\n")

p = 1
q = p + 1

steadyState = np.linalg.matrix_power(markovMatrix, p)
steadyState1 = np.linalg.matrix_power(markovMatrix, q)

while np.array_equal(np.around(steadyState, 5), np.around(steadyState1,
                                                          5)) == False:
    steadyState = np.linalg.matrix_power(markovMatrix, p)
    steadyState1 = np.linalg.matrix_power(markovMatrix, q)
    p += 1
    q = p + 1

steadyState = np.linalg.matrix_power(markovMatrix, p)

print("Steady state at: " + str(p) + " transitions")
#print(np.around(np.squeeze(steadyState), 3))
print("\n")

states1 = states
states1 = [s.replace("#", "s") for s in states1]

execcreatearray = ""
for i in range(len(states1)):
    execcreatearray = execcreatearray + "plot" + str(
        states1[i]) + " = []" + "\n"

exec(execcreatearray)

for i in range(p):
    for j in range(len(states1)):
        exec("plot" + str(states1[j]) + " = np.append(plot" + str(states1[j]) +
             ", np.squeeze(np.dot(np.linalg.matrix_power(markovMatrix, " +
             str(i) + "), startMatrix))[" + str(j) + "])")

dfexec = ""
for i in range(len(states1)):
    dfexec = dfexec + "'" + str(states1[i]) + "': plot" + str(
        states1[i]) + ", "

exec("df = pd.DataFrame({'x': range(0, " + str(p) + ")," + dfexec + "})")

plot.style.use('seaborn-white')
palette = plot.get_cmap('Set1')

num = 0
for column in df.drop('x', axis=1):
    num += 1
    plot.plot(df['x'],
              df[column],
              marker='',
              color=palette(num),
              linewidth=1,
              alpha=0.9,
              label=column)

plot.legend(loc=2, ncol=2)

plot.title("State Point Probability vs. Transition #",
           loc='center',
           fontsize=12,
           fontweight=0,
           color='black')
plot.xlabel("Transitions")
plot.ylabel("Probability")

if (os.path.exists("output/ProbabilityPlot.png") == True):
    os.remove("output/ProbabilityPlot.png")
    plot.savefig('output/ProbabilityPlot.png')
else:
    plot.savefig('output/ProbabilityPlot.png')
