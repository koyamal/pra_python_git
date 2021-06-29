r, g, b = input().split()

numAdd = r + g + b

if int(numAdd) % 4 == 0:
    print('YES')
else:
    print('NO')

