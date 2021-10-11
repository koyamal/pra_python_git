N = int(input())

As = map(int, input().split())

output = 0
for A in As:
    output += max(0, A - 10)

print(output)
