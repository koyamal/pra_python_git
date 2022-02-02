H, W = map(int, input().split())

As = []

for i in range(H):
    As.append(list(map(int, input().split())))

for j in range(W):
    output = str(As[0][j])
    for i in range(1, H):
        output += " " + str(As[i][j])
    print(output)
