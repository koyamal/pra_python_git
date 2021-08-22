N, D = map(int, input().split())

listX = []

for i in range(N):
    listX.append(list(map(int, input().split())))

output = 0
for i in range(len(listX) - 1):
    for j in range(i + 1, len(listX)):
        d = 0
        for k in range(len(listX[i])):
            d += (listX[i][k] - listX[j][k]) ** 2
        if (d ** 0.5).is_integer():
            output += 1

print(output)
