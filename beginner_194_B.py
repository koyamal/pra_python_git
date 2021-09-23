N = int(input())

As = []
Bs = []
for i in range(N):
    A, B = map(int, input().split())
    As.append([A, i])
    Bs.append([B, i])
As.sort()
Bs.sort()

if As[0][1] == Bs[0][1]:
    if As[0][0] + Bs[0][0] >= min(As[1][0], Bs[1][0]):
        print(max(max(As[0][0], Bs[0][0]), min(As[1][0], Bs[1][0])))
    else:
        print(As[0][0] + Bs[0][0])
else:
    print(max(As[0][0], Bs[0][0]))
