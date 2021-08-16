S = input()

maxLength = 0
for i in range(len(S)):
    count = 0
    for j in range(i, len(S)):
        if S[j] in "ACGT":
            count += 1
        else:
            if count >= maxLength:
                maxLength = count
            break

print(maxLength)
