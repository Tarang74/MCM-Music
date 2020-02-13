# Created by Tarang Janawalkar
# February 12, 2020

import os.path
import midiutil as mu
from midiutil.MidiFile import MIDIFile
from datetime import datetime
from markov_chain import *

date = datetime.now().strftime("%y_%m_%d_%H_%M_%S")

# create MIDI object
mf = MIDIFile(1)  # only 1 track
track = 0  # the only track

time = 0  # start at beginning
name = str(date) + "-T" + str(multPower)

mf.addTrackName(track, time, "output")
mf.addTempo(track, time, 90)

channel = 0
volume = 100

pitchArray = [
    [69, 73, 76],  # A   - A  C# E
    [69, 72, 76],  # Am  - A  C  E
    [70, 74, 77],  # A#  - A# D  F
    [70, 73, 77],  # A#m - A# C# F
    [71, 75, 78],  # B   - B  D# F#
    [71, 74, 78],  # Bm  - B  D  F#
    [72, 76, 79],  # C   - C  E  G
    [72, 75, 79],  # Cm  - C  D# G
    [73, 77, 80],  # C#  - C# F  G#
    [73, 76, 80],  # C#m - C# E  G#
    [74, 78, 81],  # D   - D  F# A
    [74, 77, 81],  # Dm  - D  F  A
    [75, 79, 82],  # D#  - D# G  A#
    [75, 78, 82],  # D#m - D# F# A#
    [76, 80, 83],  # E   - E  G# B
    [76, 79, 83],  # Em  - E  G  B
    [77, 81, 84],  # F   - F  A  C
    [77, 80, 84],  # Fm  - F  G# C
    [78, 82, 85],  # F#  - F# A# C#
    [78, 81, 85],  # F#m - F# A  C#
    [79, 83, 86],  # G   - G  B  D
    [79, 82, 86],  # Gm  - G  A# D
    [80, 84, 87],  # G#  - G# C  D#
    [80, 83, 87]
]  # G#m - G# B  D#

for i in range(len(chordGeneration)):
    a = chordGeneration[i]
    pitch1 = pitchArray[a][0]
    pitch2 = pitchArray[a][1]
    pitch3 = pitchArray[a][2]
    time = i
    duration = 1

    mf.addNote(track, channel, pitch1, time, duration, volume)
    mf.addNote(track, channel, pitch2, time, duration, volume)
    mf.addNote(track, channel, pitch3, time, duration, volume)

newdir = "output/" + name + "/"
os.makedirs(newdir)

midName = "output.mid"
with open(midName, "wb") as outfile:
    mf.writeFile(outfile)

markovMatrixExport = "MarkovMatrix.csv"
with open(markovMatrixExport, "w") as outfile:
    np.savetxt(outfile, np.squeeze(markovMatrix), fmt='%1.6f', delimiter=',')

endMatrixExport = "EndMatrix.txt"
with open(endMatrixExport, "w") as outfile:
    np.savetxt(outfile, endMatrix, fmt='%1.6f')

newMidName = "output/" + name + "/" + midName
newMarkovMatrixName = "output/" + name + "/" + markovMatrixExport
newEndMatrixName = "output/" + name + "/" + endMatrixExport

os.rename(midName, newMidName)
os.rename(markovMatrixExport, newMarkovMatrixName)
os.rename(endMatrixExport, newEndMatrixName)

print(dash)
print("Process completed.")
print(dash)
