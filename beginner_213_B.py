input()
As = list(map(int, input().split()))

index = [0, 0]
maxA = [0, 0]

for i in range(len(As)):
    if maxA[0] < As[i]:
        maxA[0], maxA[1] = As[i], maxA[0]
        index[0], index[1] = i, index[0]
    elif maxA[1] < As[i]:
        maxA[1] = As[i]
        index[1] = i

print(index[1] + 1)
