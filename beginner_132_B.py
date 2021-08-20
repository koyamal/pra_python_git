n = input()
ps = list(map(int, input().split()))

count = 0
for i in range(1, len(ps) - 1):
    if ps[i - 1] < ps[i] < ps[i + 1] or ps[i + 1] < ps[i] < ps[i - 1]:
        count += 1

print(count)
