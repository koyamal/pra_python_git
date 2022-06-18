N, K = map(int, input().split())
As = list(map(int, input().split()))
XYs = []
for _ in range(N):
    X, Y = map(int, input().split())
    XYs.append([X, Y])

max = 0
for i in range(N):
    min = 10 ** 10 ** 2
    for j in range(K):
            if (XYs[As[j] - 1][0] - XYs[i][0]) ** 2 + (XYs[As[j] - 1][1] - XYs[i][1]) ** 2 < min:
                min = (XYs[As[j] - 1][0] - XYs[i][0]) ** 2 + (XYs[As[j] - 1][1] - XYs[i][1]) ** 2
    if min > max:
        max = min

print(max ** 0.5)
