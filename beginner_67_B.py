N, K = map(int, input().split())

Ls = list(map(int, input().split()))

Ls.sort(reverse=True)

output = 0
for i in range(K):
    output += Ls[i]

print(output)

