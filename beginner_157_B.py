sizeCard = 3
listAs = [list(map(int, input().split())), list(map(int, input().split())), list(map(int, input().split()))]
selectedNumber = [["*" for j in range(sizeCard)] for i in range(sizeCard)]
N = int(input())

for _ in range(N):
    b = int(input())
    flag = True
    for i in range(len(listAs)):
        if flag:
            for j in range(len(listAs[i])):
                if b == listAs[i][j]:
                    selectedNumber[i][j] = "o"
                    flag = False
                    break

if ["o" for i in range(sizeCard)] in selectedNumber:
    print("Yes")
    exit()

count_A = 0
count_B = 0
for i in range(len(selectedNumber)):
    if selectedNumber[i][i] == "o":
        count_A += 1
    if selectedNumber[i][len(selectedNumber) - i - 1] == "o":
        count_B += 1
if count_A == sizeCard or count_B == sizeCard:
    print("Yes")
    exit()

for i in range(len(selectedNumber[0])):
    count = 0
    for j in range(len(selectedNumber)):
        if selectedNumber[j][i] == "o":
            count += 1
    if count == sizeCard:
        print("Yes")
        exit()

print("No")
