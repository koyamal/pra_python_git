N = int(input())
anslist = map(int, input().split())
box = []

for i in range(1, 250):
    for j in range(1, 250):
        c = 4 * i * j + 3 * i + 3 * j
        if c <= 1000:
            box.append(c)

count = 0
for ans in anslist:
    if ans not in box:
        count += 1

print(count)
