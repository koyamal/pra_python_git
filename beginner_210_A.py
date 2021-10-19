N, A, X, Y = map(int, input().split())

output = 0

if N <= A:
    output = X * N
else:
    output = A * X + Y * (N - A)

print(output)
