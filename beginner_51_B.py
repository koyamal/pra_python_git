K, S = map(int, input().split())

count = 0
for x in range(K + 1):
    for y in range(K + 1):
        if K >= S - x - y >= 0:
            count = count + 1


print(count)
