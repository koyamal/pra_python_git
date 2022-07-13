import  math
a, b, d = map(int, input().split())

r = (a ** 2 + b ** 2) ** 0.5
print(a * math.cos(math.radians(d)) - b * math.sin(math.radians(d)), a * math.sin(math.radians(d)) + b * math.cos(math.radians(d)))