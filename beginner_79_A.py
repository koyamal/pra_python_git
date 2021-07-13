N = input()
count = 0
for i in range(3):
    if N[i] == N[i + 1]:
        count += 1
        if count >= 2:
            print('Yes')
            exit()
    else:
        count = 0

print('No')
