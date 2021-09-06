N, D = map(int, input().split())

output = 0

for _ in range(N):
    X, Y = map(int, input().split())
    if X ** 2 + Y ** 2 <= D ** 2:
        output += 1

print(output)
