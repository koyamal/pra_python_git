S = input()

output = []
for i in range(len(S)):
    if S[i] == 'A':
        output.append(i)
        break

for i in range(len(S)):
    if S[len(S) - 1 - i] == 'Z':
        output.append(len(S) - 1 - i)
        break

print(output[1] - output[0] + 1)
