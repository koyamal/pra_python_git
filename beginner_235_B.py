N = int(input())

Hs = list(map(int, input().split()))
max = 0
for h in Hs:
    if h > max:
        max = h
    else:
        print(max)
        exit()

print(max)
