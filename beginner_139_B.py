A, B = map(int, input().split())

quot = B // (A - 1)

output = A
count = 1
for i in range(quot):
    if output >= B:
        print(count)
        exit()
    output += A - 1
    count += 1
print(count)
