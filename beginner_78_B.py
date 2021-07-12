X, Y, Z = map(int, input().split())

q = X // (Y + Z)
if X % (Y + Z) >= Z:
    print(X // (Y + Z))
else:
    print(-1 + (X // (Y + Z)))
    