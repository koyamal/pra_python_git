N = int(input())
ds = list(map(int, input().split()))

output = 0

for i in range(N - 1):
    for j in range(i + 1, N):
        output += ds[i] * ds[j]

print(output)
