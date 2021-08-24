S = input()

for i in range(len(S)):
    if (i + 1) % 2 == 1 and S[i] not in "RUD":
        print("No")
        exit()
    if (i + 1) % 2 == 0 and S[i] not in "LUD":
        print("No")
        exit()

print("Yes")
