N = int(input())

quot = N // 2

if N % 2 == 1:
    print((quot + 1) / N)
else:
    print(quot / N)
