As = []
Bs = []
N, M = map(int, input().split())

for i in range(N):
    As.append(input())
for i in range(M):
    Bs.append(input())

startPoint = []
for k, A in enumerate(As[:len(As) - len(Bs) + 1]):
    a = 0
    for B in Bs:
        if a == 0 and B in A:
            for i in range(len(As) - len(Bs) + 1):
                if B in A[i:i + len(B)]:
                    startPoint.append(i)
        elif a != 0 and B in As[k + a]:
            for i in startPoint:
                if B not in As[k + a][i:i + len(B)]:
                    startPoint.remove(i)
        elif B not in As[k + a]:
            startPoint.clear()
            break
        a = a + 1

    if len(startPoint) > 0:
        break

if len(startPoint) > 0:
    print('Yes')
else:
    print('No')
