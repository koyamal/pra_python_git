N = int(input())

d = {}

for _ in range(N):
    S = input()
    if S in d:
        d[S] += 1
    else:
        d[S] = 1

print(max(d, key=d.get))
