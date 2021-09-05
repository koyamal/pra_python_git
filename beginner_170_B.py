X, Y = map(int, input().split())

for i in range(0, X + 1):
    if i * 4 + (X - i) * 2 == Y:
        print("Yes")
        exit()

print("No")