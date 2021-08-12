N = int(input())

count8divisors = 0
for i in range(1, N + 1):
    if i % 2 == 0:
        continue
    countDivisor = 0
    for j in range(1, i + 1):
        if i % j == 0:
            countDivisor += 1
    if countDivisor == 8:
        count8divisors += 1

print(count8divisors)
