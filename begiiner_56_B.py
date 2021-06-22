W, a, b = map(int, input().split())

xA = [a, a + W]
xB = [b, b + W]

if a <= b <= a + W or a <= b + W <= a + W:
    print(0)
else:
    print(min(abs(a - b - W), abs(a + W - b)))
