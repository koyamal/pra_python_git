S = input()
T = input()

hp = 1
for i in range(len(S) - 1):
    if S[i] != T[i]:
        if S[i] == T[i + 1] and S[i + 1] == T[i]:
            hp -= 1
        else:
            print("No")
            exit()

if S == T or hp == 0:
    print("Yes")
else:
    print("No")
    