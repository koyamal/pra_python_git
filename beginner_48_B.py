a, b, x = map(int, input().split())

#max = b - (b % x)
max = b // x

if a % x == 0:
    min_ = a
else:
    min_ = a + x - (a % x)

min = min_ // x

if max <= min:
    print(0)
else:
    print(1 + max - min)



