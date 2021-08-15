S = input()

minDiff = 753

for i in range(len(S) - 2):
    tempS = S[i: i + 3]
    if abs(753 - int(tempS)) < minDiff:
        minDiff = abs(753 - int(tempS))

print(minDiff)

