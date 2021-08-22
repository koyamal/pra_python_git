N = int(input())

Ps = list(map(int, input().split()))

Ns = [i for i in range(1, N + 1)]

count = 0
for i in range(N):
    if Ns[i] != Ps[i]:
        count += 1

if count == 0 or count == 2:
    print("YES")
else:
    print("NO")
