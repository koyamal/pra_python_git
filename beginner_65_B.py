N = int(input())
listA = []
indexShinedLight = [1]
for i in range(N):
    listA.append(int(input()))

tempIndex = 1
count = 0
while count < N:
    if tempIndex == 2:
        print(count)
        exit()
    else:
        tempIndex = listA[tempIndex - 1]
        count += 1

print(-1)

