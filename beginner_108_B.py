x1, y1, x2, y2 = map(int, input().split())

x3, y3, x4, y4 = 0, 0, 0, 0
if x1 == x2:
    if y1 > y2:
        x3 = x2 + (y1 - y2)
        y3 = y2
        x4 = x3
        y4 = x1
    else:
        x3 = x2 - (y2 - y1)
        y3 = y2
        x4 = x3
        y4 = y1
else:
    if x1 > x2:
        x3 = x2
        y3 = y2 - (x1 - x2)
        x4 = x1
        y4 = y3
    else:
        x3 = x2
        y3 = y2 + (x2 - x1)
        x4 = x1
        y4 = y3

print(x3, y3, x4, y4)
