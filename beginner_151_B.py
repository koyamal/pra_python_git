N, K, M = map(int, input().split())
As = list(map(int, input().split()))

diffTarget = M * N - sum(As)

if diffTarget <= K:
    print(max(diffTarget, 0))
else:
    print(-1)
