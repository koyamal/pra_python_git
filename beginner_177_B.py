S = input()
T = input()

minDiff = len(T)

for i in range(1 + len(S) - len(T)):
    count = 0
    for j in range(len(T)):
        if S[i + j] != T[j]:
            count += 1
    if count < minDiff:
        minDiff = count

print(minDiff)
