N = int(input())

output = 0
maxValue = 0
for i in range(N):
    p = int(input())
    output += p
    if p > maxValue:
        maxValue = p

output -= maxValue / 2

print(int(output))
