N = int(input())
listA = []
indexShinedLight = [1]
for i in range(N):
    listA.append(input())

shineSecond = True

tempIndex = 1
while shineSecond:
    tempIndex = int(listA[tempIndex - 1])
    if tempIndex in indexShinedLight:
        shineSecond = False
        print(-1)
        exit()

    if tempIndex == 2:
        shineSecond = False
        print(len(indexShinedLight))
        exit()

    indexShinedLight.append(tempIndex)

