S = input()

for i in range(0, len(S) - 2, 2):
    if not S[i].islower():
        print("No")
        exit()
    if not S[i + 1].isupper():
        print("No")
        exit()

if len(S) % 2 == 0:
    if not S[len(S) - 2].islower():
        print("No")
        exit()
    if not S[len(S) - 1].isupper():
        print("No")
        exit()
else:
    if not S[len(S) - 1].islower():
        print("No")
        exit()
print("Yes")
