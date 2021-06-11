N = int(input())
K = int(input())
X = int(input())
Y = int(input())

output = 0
if N <= K:
    output = X * N
else:
    output = X * K + Y * (N - K)

print(output)