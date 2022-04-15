x = []
y = []
for _ in range(3):
    tempX, tempY = map(int, input().split())
    x.append(tempX)
    y.append(tempY)

outputX = 0
outputY = 0
if x[0] == x[1]:
    outputX = x[2]
elif x[1] == x[2]:
    outputX = x[0]
else:
    outputX = x[1]

if y[0] == y[1]:
    outputY = y[2]
elif y[1] == y[2]:
    outputY = y[0]
else:
    outputY = y[1]

print(outputX, outputY)
