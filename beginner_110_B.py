N, M, X, Y = map(int, input().split())
xs = list(map(int, input().split()))
ys = list(map(int, input().split()))

first = set([i for i in range(X + 1, Y + 1)])

second = set([i for i in range(max(xs) + 1, 101)])

third = set([i for i in range(-100, min(ys) + 1)])

if len(first & second & third) == 0:
    print("War")
else:
    print("No War")
