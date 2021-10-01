H, W, X, Y = map(int, input().split())
Ss = []

for _ in range(H):
    Ss.append(input())

output = -1
for i in range(Y - 1):
    if Ss[X - 1][Y - 2 - i] == ".":
        output += 1
    else:
        break

for i in range(Y - 1, W):
    if Ss[X - 1][i] == ".":
        output += 1
    else:
        break

for i in range(X - 1):
    if Ss[X - 2 - i][Y - 1] == ".":
        output += 1
    else:
        break

for i in range(X - 1, H):
    if Ss[i][Y - 1] == ".":
        output += 1
    else:
        break

print(output)
