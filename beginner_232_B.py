S = input()
T = input()

diff = ord(T[0]) - ord(S[0])

for i in range(len(S)):
    if str(ord(S[i]) + diff) != T[0]:
        print("No")
        exit()

print("Yes")
