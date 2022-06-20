N = int(input())
As = list(map(int, input().split()))

P = 0
for i in range(N):
    sumA = sum(As[i:N])
    if sumA >= 4:
        P += 1

print(P)
