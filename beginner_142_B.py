N, K = map(int, input().split())
hs = list(map(int, input().split()))

output = 0

for h in hs:
    if h >= K:
        output += 1

print(output)
