N = int(input())

As = list(map(int, input().split()))

d = {n: 4 for n in range(1, N+1)}

for a in As:
    d[a] -= 1

for k, v in d.items():
    if v == 1:
        print(k)
