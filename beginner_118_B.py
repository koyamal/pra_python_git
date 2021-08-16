N, M = map(int, input().split())

output = set(range(1, M + 1))

for i in range(N):
    tempList = list(map(int, input().split()))
    tempSet = set()
    for j in range(1, len(tempList)):
        tempSet.add(tempList[j])
    output = output & tempSet

print(len(output))
