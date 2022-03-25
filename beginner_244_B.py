N = int(input())
T = input()

p = [0, 0]
d = [1, 0, 0, 0]

for t in T:
    if t == "R":
        if d[0] == 1:
            d = [0, 0, 0, 1]
        elif d[1] == 1:
            d = [0, 0, 1, 0]
        elif d[2] == 1:
            d = [1, 0, 0, 0]
        else:
            d = [0, 1, 0, 0]
    else:
        p[0] = p[0] + d[0] - d[1]
        p[1] = p[1] + d[2] - d[3]

print(p[0], p[1])
