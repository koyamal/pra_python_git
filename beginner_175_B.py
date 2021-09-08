input()
Ls = list(map(int, input().split()))

output = 0
for i in range(len(Ls) - 2):
    for j in range(i + 1, len(Ls) - 1):
        for k in range(j + 1, len(Ls)):
            if Ls[i] + Ls[j] > Ls[k] and Ls[j] + Ls[k] > Ls[i] and Ls[k] + Ls[i] > Ls[j] and Ls[k] != Ls[i] and \
                    Ls[i] != Ls[j] and Ls[k] != Ls[j]:
                output += 1

print(output)
