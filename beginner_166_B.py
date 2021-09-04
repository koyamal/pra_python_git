N, K = map(int, input().split())

setHaveTreat = set()
setAll = {i for i in range(1, N + 1)}
for i in range(K):
    input()
    setHaveTreat = setHaveTreat | set(map(int, input().split()))

print(len(setAll - setHaveTreat))
