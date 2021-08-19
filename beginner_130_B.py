N, X = map(int, input().split())
Ls = list(map(int, input().split()))

output = 1
D = 0
for L in Ls:
    D += L
    if D > X:
        print(output)
        exit()
    output += 1
