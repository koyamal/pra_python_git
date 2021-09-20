V, T, S, D = map(int, input().split())

if V * T > D or S * V < D:
    print("Yes")
else:
    print("No")
