C = input()

for i in range(1, len(C)):
    if C[0] != C[i]:
        print("Lost")
        exit()

print("Won")
