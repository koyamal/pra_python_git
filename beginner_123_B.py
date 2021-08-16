minDiff = 10
output = 0
for i in range(5):
    temp = int(input())
    if temp % 10 != 0:
        if temp % 10 < minDiff:
            minDiff = temp % 10
        output += 10 * ((temp // 10) + 1)
    else:
        output += temp

print(output - (10 - minDiff))

