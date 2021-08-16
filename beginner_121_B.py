N, M, C = map(int, input().split())
Bs = list(map(int, input().split()))

output = 0
for i in range(N):
    As = list(map(int, input().split()))
    sumAB = C
    for j in range(len(As)):
        sumAB += As[j] * Bs[j]
    if sumAB > 0:
        output += 1

print(output)
