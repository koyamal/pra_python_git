P = int(input())

output = 0

for i in range(10, 0, -1):
    value = 1
    for j in range(1, i + 1):
        value *= j
    n = P // value
    P -= n * value
    output += n
    if P == 0:
        print(output)
        exit()
