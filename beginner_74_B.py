N = int(input())
K = int(input())

xlist = list(map(int, input().split()))

output = 0

for x in xlist:
    output += 2 * min(x, K - x)

print(output)
