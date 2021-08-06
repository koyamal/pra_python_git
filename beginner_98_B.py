N = int(input())
S = input()

maxValue = 0
for i in range(N):
    frontS = S[:i]
    backS = S[i:]
    maxValue = max(maxValue, len(set(frontS) & set(backS)))

print(maxValue)
