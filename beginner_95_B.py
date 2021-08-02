N, X = map(int, input().split())

mlist = []
for i in range(N):
    mlist.append(int(input()))

print(N + ((X - sum(mlist)) // min(mlist)))
