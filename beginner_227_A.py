N, K, A = map(int, input().split())

listP = []
for i in range(A, N + 1):
    listP.append(i)

for i in range(1, A):
    listP.append(i)

if len(listP) < K:
    print(listP[len(listP) - 1])
else:
    print(listP[K - 1])
