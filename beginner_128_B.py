N = int(input())
SPIndexs = []

for i in range(N):
    s, p = input().split()
    SPIndexs.append([s, int(p), i + 1])

SPIndexs.sort(key=lambda x: x[1], reverse=True)
SPIndexs.sort(key=lambda x: x[0])

for SPIndex in SPIndexs:
    print(SPIndex[2])
