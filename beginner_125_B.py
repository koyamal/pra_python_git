N = int(input())
Vs = list(map(int, input().split()))
Cs = list(map(int, input().split()))

output = 0
for i in range(N):
    tempDiff = Vs[i] - Cs[i]
    if tempDiff > 0:
        output += tempDiff

print(output)
