S = input()
T = input()

output = 0
for i in range(len(S)):
    if S[i] == T[i]:
        output += 1

print(output)
