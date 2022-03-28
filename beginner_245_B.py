input()

As = list(set(map(int, input().split())))

As.sort()

for i in range(max(As) + 2):
    if i not in As:
        print(i)
        exit()
