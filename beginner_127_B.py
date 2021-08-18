r, D, x2000 = map(int, input().split())

previousX = x2000
for i in range(10):
    X = r * previousX - D
    print(X)
    previousX = X
