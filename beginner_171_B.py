N, K = map(int ,input().split())
ps = list(map(int, input().split()))

ps.sort()

output = 0

for i in range(K):
    output += ps[i]

print(output)
