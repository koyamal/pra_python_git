N, X, T = map(int, input().split())

num = N // X

if N % X == 0:
    print(num * T)
else:
    print((num + 1) * T)
