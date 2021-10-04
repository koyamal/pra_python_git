N = int(input())

As = map(int, input().split())
Bs = map(int, input().split())

maxA = max(As)
minB = min(Bs)

if minB - maxA >= 0:
    print(minB - maxA + 1)
else:
    print(0)
