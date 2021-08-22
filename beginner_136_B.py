N = input()

output = 0

for i in range(int(N)):
    if len(str(i + 1)) % 2 == 1:
        output += 1

print(output)
