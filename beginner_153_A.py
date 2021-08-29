H, A = map(int, input().split())

if H % A == 0:
    print(H // A)
else:
    print(1 + H // A)
