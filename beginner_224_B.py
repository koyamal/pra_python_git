H, W = map(int, input().split())
As = []
for _ in range(H):
    As.append(list(map(int, input().split())))

for i1 in range(H - 1):
    for i2 in range(i1 + 1, H):
        for j1 in range(W - 1):
            for j2 in range(j1, W):
                if As[i1][j1] + As[i2][j2] > As[i1][j2] + As[i2][j1]:
                    print("No")
                    exit()

print("Yes")
