AB = []
AB.append(int(input()))
AB.append(int(input()))

for i in range(3):
    if (i + 1) not in AB:
        print(i + 1)
