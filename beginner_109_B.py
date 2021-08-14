N = int(input())

Ws = []
for i in range(N):
    tempW = input()
    if tempW in Ws:
        print("No")
        exit()

    Ws.append(tempW)

lastCharacter = Ws[0][0]

for W in Ws:
    if lastCharacter == W[0]:
        lastCharacter = W[len(W) - 1]
    else:
        print("No")
        exit()

print("Yes")
