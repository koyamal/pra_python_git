N, K = map(int, input().split())
As = list(map(int, input().split()))
XYs = []
for _ in range(N):
    X, Y = map(int, input().split())
    XYs.append([X, Y])

max = 0
for i in range(N - 1):
    min = 10 ** 10
    for j in range(i+1, N):
        if (XYs[i][0] - XYs[j][0]) ** 2 + (XYs[i][1] - XYs[j][1]) ** 2 < min:
            min = (XYs[i][0] - XYs[j][0]) ** 2 + (XYs[i][1] - XYs[j][1]) ** 2
    if min > max:
        max = min

print(min ** 0.5)
