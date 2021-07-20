a, b = input().split()

N = int(a + b)

if (N ** 0.5).is_integer():
    print('Yes')
else:
    print('No')
