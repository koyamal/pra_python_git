S = input()

output = 0

for i in S:
    if i == "+":
        output += 1
    else:
        output -= 1

print(output)
