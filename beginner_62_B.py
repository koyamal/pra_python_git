H, W = map(int, input().split())

As = []

for i in range(H):
    As.append(input())

flLine = '#' * (W + 2)

print(flLine)
for A in As:
    print('#' + A + '#')
print(flLine)
