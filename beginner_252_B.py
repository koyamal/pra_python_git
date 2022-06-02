N, K = map(int, input().split())
As = list(map(int, input().split()))
Bs = list(map(int, input().split()))

Hs = []
for B in Bs:
    Hs.append(As[B - 1])

if max(As) in Hs:
    print("Yes")
else:
    print("No")
