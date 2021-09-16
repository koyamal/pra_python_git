N = int(input())

xy = []
for _ in range(N):
    x, y = map(int, input().split())
    xy.append([x, y])

output = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        if -1 <= (xy[i][1] - xy[j][1]) / (xy[i][0] - xy[j][0]) <= 1:
            output += 1

print(output)
