N, M = map(int, input().split())
UV = []

for _ in range(M):
    UV.append(list(map(int, input().split())))

output = 0
for i in range(M - 2):
    for j in range(i + 1, M - 1):
        if UV[i][0] == UV[j][0]:
            if ([UV[i][1], UV[j][1]] in UV) or ([UV[j][1], UV[i][1]] in UV):
                output += 1
                break
        elif UV[i][0] == UV[j][1]:
            if ([UV[i][1], UV[j][0]] in UV) or ([UV[j][0], UV[i][1]] in UV):
                output += 1
                break
        elif UV[i][1] == UV[j][0]:
            if ([UV[i][0], UV[j][1]] in UV) or ([UV[j][1], UV[i][0]] in UV):
                output += 1
                break
        elif UV[i][1] == UV[j][1]:
            if ([UV[i][0], UV[j][0]] in UV) or ([UV[j][0], UV[i][0]] in UV):
                output += 1
                break

print(output)
