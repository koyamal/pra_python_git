N = int(input())

for i in range(9):
    if N == (i + 1) * (N // (i + 1)) and (N // (i + 1)) <= 9:
        print("Yes")
        exit()

print("No")
