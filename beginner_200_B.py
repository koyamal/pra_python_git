N, K = input().split()

for _ in range(int(K)):
    if int(N) % 200 == 0:
        N = str(int(N) // 200)
    else:
        N = N + "200"

print(N)
