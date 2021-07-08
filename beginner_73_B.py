N = int(input())

output = 0

for i in range(N):
    l, r = map(int, input().split())
    output += r - l + 1

print(output)
