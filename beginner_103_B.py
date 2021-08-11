S = input()
T = input()

for i in range(len(S)):
    tempS = S[len(S) - 1]
    S = tempS + S[:len(S) - 1]
    if S == T:
        print("Yes")
        exit()

print("No")
