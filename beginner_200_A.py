N = int(input())

if N % 100 == 0:
    print(N // 100)
else:
    print(1 + N // 100)
