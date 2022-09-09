N, M = map(int, input().split())
UV = []

for _ in range(M):
    UV.append(list(map(int, input().split())))

output = 0
for i in range(M - 2):
    for j in range(i + 1, M - 1):
        s = set(UV[i] + UV[j])
        if len(s) != 4:
            for k in range(j + 1, M):
                ss = set(UV[i] + UV[j] + UV[k])
                if len(ss) == 3:
                    output += 1

print(output)
