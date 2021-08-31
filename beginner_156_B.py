K, N = map(int, input().split())

output = 0
quot = K
while True:
    quot = quot // N
    output += 1
    if quot == 0:
        break

print(output)
