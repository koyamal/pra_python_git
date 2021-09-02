N = int(input())

output = 0
for i in range(1, N + 1):
    if i % 3 != 0 and i % 5 != 0:
        output += i

print(output)
