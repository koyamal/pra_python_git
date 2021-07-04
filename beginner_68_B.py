N = int(input())

maxTow = 0
fTwo = False
output = 0
for i in range(N):
    qT = N - i
    count = 0
    while qT % 2 == 0:
        count += 1
        if qT == 2:
            fTwo = True
            break
        qT /= 2
    if maxTow < count:
        maxTow = count
        output = N - i
    if fTwo:
        break

if N == 1:
    print(1)
else:
    print(output)

