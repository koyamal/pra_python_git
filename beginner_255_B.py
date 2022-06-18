N, K = map(int, input().split())
As = list(map(int, input().split()))
XYs = []
for _ in range(N):
    X, Y = map(int, input().split())
    XYs.append([X, Y])

max = 0
for i in range(K):
    min = 10 ** 10
    for j in range(N):
        if(As[i] - 1 != j):
            if (XYs[As[i] - 1][0] - XYs[j][0]) ** 2 + (XYs[As[i] - 1][1] - XYs[j][1]) ** 2 < min:
                min = (XYs[As[i] - 1][0] - XYs[j][0]) ** 2 + (XYs[As[i] - 1][1] - XYs[j][1]) ** 2
    if min > max:
        max = min

print(min ** 0.5)
