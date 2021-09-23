N = int(input())

minP = 10 ** 9 + 1
canBuy = False
for _ in range(N):
    A, P, X = map(int, input().split())
    if X - A > 0 and minP > P:
        minP = P
        canBuy = True

if canBuy:
    print(minP)
else:
    print(-1)
