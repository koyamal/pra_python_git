N = int(input())

d = []
for i in range(N):
    d.append(list(map(int, input().split())))

max = 0

for i in range(N - 1):
    for j in range(i + 1, N):
        dist = ((d[i][0] - d[j][0]) ** 2 + (d[i][1] - d[j][1]) ** 2) ** 0.5
        if dist > max:
            max = dist

print(max)
