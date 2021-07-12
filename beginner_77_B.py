N = int(input())

output = 0
for i in range(N + 1):
    if i * i > N:
        break
    output = i * i

print(output)
