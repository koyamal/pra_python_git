a, b = map(int, input().split())

diffHigh = b - a

output = 0
for i in range(diffHigh):
    output += i + 1

print(output - b)
