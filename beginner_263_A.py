ABCDE = list(map(int, input().split()))
box = []

for s in ABCDE:
    if s not in box:
        box.append(s)

if len(box) != 2:
    print('No')
    exit()
else:
    count = 0
    for s in ABCDE:
        if s == box[0]:
            count += 1
    if count == 2 or count == 3:
        print('Yes')
        exit()
    else:
        print('No')
        exit()
