N, A, B = map(int, input().split())

output = 0
for i in range(N):
    sumI = 0
    strI = str(i + 1)
    for j in strI:
        sumI += int(j)

    if A <= sumI <= B:
        output += i + 1

print(output)
