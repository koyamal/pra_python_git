N = int(input())

output = 0

for i in range(1, N + 1):
    output += i
    if output >= N:
        print(i)
        exit()
