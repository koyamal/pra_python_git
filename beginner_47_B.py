W, H, N = map(int, input().split())

xyas = []
for i in range(N):
    xyas.append(list(map(int, input().split())))

x_min, x_max, y_min, y_max = (0, W, 0, H)

for xya in xyas:
    if xya[2] == 1:
        if x_min < xya[0]:
            x_min = xya[0]
    elif xya[2] == 2:
        if x_max > xya[0]:
            x_max = xya[0]
    elif xya[2] == 3:
        if y_min < xya[1]:
            y_min = xya[1]
    else:
        if y_max > xya[1]:
            y_max = xya[1]


print(max(0, (x_max - x_min)) * max(0, (y_max - y_min)))
