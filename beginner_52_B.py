N = int(input())
S = input()

x = 0
max_x = 0

for i in S:
    if i == 'I':
        x = x + 1
    else:
        x = x - 1

    if x > max_x:
        max_x = x

print(max_x)
