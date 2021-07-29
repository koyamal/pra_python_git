N, M, X = map(int, input().split())
listA = list(map(int, input().split()))

left = 0
right = 0
for A in listA:
    if A < X:
        left += 1
    if A > X:
        right += 1

print(min(left, right))
