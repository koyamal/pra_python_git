a, b, x = map(int, input().split())

max = b - (b % x)

if a % x == 0:
    min = a
else:
    min = a + x - (a % x)

if max <= min:
    print(0)
else:
    print(1 + int(max/x - min/x))


#print(min, max/x)
#print(int(max/x))
#print(max)


