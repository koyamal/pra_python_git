A, B, C, D = map(int, input().split())

if B < C * D:
    if A % (C * D - B) == 0:
        print(A // (C * D - B))
    else:
        print(1 + A // (C * D - B))
else:
    print(-1)
