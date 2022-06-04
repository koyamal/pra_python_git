H, W = map(int, input().split())

point = []
for i in range(H):
    s = input()
    for j in range(len(s)):
        if s[j] == 'o':
            point.append([i, j])

print(abs(point[0][0] - point[1][0])+abs(point[0][1] - point[1][1]))
