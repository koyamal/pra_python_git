x1, y1, x2, y2 = map(int, input().split())

A = x2 - x1
B = y2 - y1

x3 = x2 - B
y3 = y2 + A
x4 = x1 - B
y4 = y1 + A

print(x3, y3, x4, y4)
