listS = []
listS.append(input())
listS.append(input())
listS.append(input())

T = input()

output = ""
for i in T:
    output += listS[int(i) - 1]

print(output)
