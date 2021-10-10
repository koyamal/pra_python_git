N, K = map(int, input().split())

output = 0
for i in range(1, N + 1):
    for k in range(1, K + 1):
        output += int(str(i) + "0" + str(k))

print(output)
