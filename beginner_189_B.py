N, X = map(int, input().split())
X *= 100 * X
sumA = 0
for i in range(N):
    V, P = map(int, input().split())
    sumA += V * P
    if sumA > X:
        print(i + 1)
        exit()
print(-1)
