N = int(input())
As = list(map(int, input().split()))
Bs = list(map(int, input().split()))
Cs = list(map(int, input().split()))

output = 0
for i in range(N):
    output += Bs[As[i] - 1]
    if As[i] == As[i - 1] + 1 and i > 0:
        output += Cs[As[i - 1] - 1]

print(output)

