N, M = map(int, input().split())

listIndex = [i + 1 for i in range(N)]
listNumber = []
for i in range(M):
    a, b = map(int, input().split())
    listNumber.append(a)
    listNumber.append(b)

for i in range(N):
    print(listNumber.count(listIndex[i]))

