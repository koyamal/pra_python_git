Os = input()
Es = input()

output = ''
for i, O in enumerate(Os):
    if i == len(Os) - 1:
        if len(Es) <= i:
            output += O
            break

    output += O + Es[i]

print(output)
