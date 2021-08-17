N = int(input())
Hs = list(map(int, input().split()))

maxHeight = 0

count = 0
for H in Hs:
    if H >= maxHeight:
        maxHeight = H
        count += 1

print(count)
