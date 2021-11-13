S = input()

listS = []
for i in range(len(S)):
    listS.append(S[i:] + S[:i])

print(min(listS))
print(max(listS))
