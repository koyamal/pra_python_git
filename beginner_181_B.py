N = int(input())

output = 0
for _ in range(N):
    A, B = map(int, input().split())
    for i in range(A, B + 1):
        output += i

print(output)
