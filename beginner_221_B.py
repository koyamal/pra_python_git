S = input()
T = input()

hp = 0
count = 0
for i in range(len(S) - 1):
    if S[i] != T[i]:
        if S[i] == T[i + 1] and S[i + 1] == T[i] and hp == 0:
            hp += 1
        else:
            count += 1

if S == T or (hp == 1 and count <= 1):
    print("Yes")
else:
    print("No")
