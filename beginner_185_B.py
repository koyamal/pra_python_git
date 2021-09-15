N, M, T = map(int, input().split())

size = N
preB = 0
for _ in range(M):
    A, B = map(int, input().split())
    N = N - (A - preB)
    if N <= 0:
        print("No")
        exit()
    N = min(size, N + (B - A))
    preB = B

N = N - (T - preB)
if N <= 0:
    print("No")
    exit()

print("Yes")
