input()
As = list(map(int, input().split()))

maxGCD = 0
maxIndex = 2

for i in range(2, max(As) + 1):
    count = 0
    for A in As:
        if A % i == 0:
            count += 1
    if count > maxGCD:
        maxGCD = count
        maxIndex = i

print(maxIndex)
