N = int(input())

output = 0
for _ in range(N):
    A, B = map(int, input().split())
    output += int((B - A + 1) * (A + B) / 2)

print(output)
