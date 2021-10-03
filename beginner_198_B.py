N = input()

for i in range(len(N)):
    if N[len(N) - 1 - i] == "0":
        N = N.rstrip("0")
    else:
        break

flagC = True
for i in range(len(N) // 2):
    if N[i] != N[len(N) - 1 - i]:
        flagC = False
        break

if flagC:
    print("Yes")
else:
    print("No")
