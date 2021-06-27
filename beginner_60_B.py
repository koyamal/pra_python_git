A, B, C = map(int, input().split())

rest = []
for i in range(B):
    R = (A * (i + 1)) % B
    if R == 0:
        break

    if R not in rest:
        rest.append(R)

print(rest)

