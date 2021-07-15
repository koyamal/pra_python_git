N = input()
As = list(map(int, input().split()))

output = 0
while True:
    for i, A in enumerate(As):
        if A % 2 != 0:
            print(output)
            exit()
        As[i] = A / 2

    output += 1

print(output)
