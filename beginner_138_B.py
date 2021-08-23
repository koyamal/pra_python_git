input()
As = list(map(int, input().split()))

sumReciprocal = 0

for A in As:
    sumReciprocal += 1 / A

print(1 / sumReciprocal)
