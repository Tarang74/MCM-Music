import numpy as np
states = ["A", "C#m"]
markov = np.array([[3 / 7, 3 / 4], [4 / 7, 1 / 4]])
print(markov)

startState = np.array([[1], [0]])
print(startState)

multiply = np.dot(markov, startState)

print(multiply)

power = int(input("Number of transitions: ")) + 1

multiplyPower = np.linalg.matrix_power(markov, power)
print(multiplyPower)

statesIndex = np.arange(0, 2)
final = np.zeros(power, dtype=int)

for i in range(0, power):
    prob = np.dot(np.linalg.matrix_power(markov, i), startState)
    prob = np.squeeze(prob).tolist()
    final[i] = np.random.choice(statesIndex, p=prob)
    print("It no: ", i)
    print(np.round(prob, 4))  # Each column matrix probability
    print("\n")

print(final)

finalChords = [""] * power

for i in range(len(final)):
    a = final[i]
    finalChords[i] = states[a]
print(finalChords)