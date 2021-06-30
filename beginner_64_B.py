input()
listA = map(int, input().split())

maxA = 0
minA = 1000

for A in listA:
    if A > maxA:
        maxA = A
    if A < minA:
        minA = A

print(maxA - minA)
