N, X = map(int, input().split())

sumA = 0
for i in range(N):
    V, P = map(int, input().split())
    sumA += V * P * 0.01
    if sumA > X:
        print(i + 1)
        exit()
print(-1)
