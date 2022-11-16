X, Y, N = map(int ,input().split())

if X <= Y / 3.0:
    print(X * N)
else:
    numY = N // 3
    numX = N - numY * 3
    print(numY * Y + numX * X)

print("Hello World")
