N, X = map(int, input().split())

for i in range(ord('A'), ord('Z') + 1):
    if((i - ord('A') + 1) * N > X):
        print(chr(i - 1))
        exit()
