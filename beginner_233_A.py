X, Y = map(int, input().split())

if X >= Y:
    print(0)
else:
    diff = Y - X
    ans = diff // 10
    if diff % 10 == 0:
        print(ans)
    else:
        print(ans + 1)
