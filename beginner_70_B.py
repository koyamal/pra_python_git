A, B, C, D = map(int, input().split())

output = 0
for i in range(C, D):
    if A <= i <= B:
        output += 1

print(output)
