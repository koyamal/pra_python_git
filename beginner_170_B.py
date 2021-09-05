xs = list(input().split())

for i in range(len(xs)):
    if xs[i] == "0":
        print(i + 1)
        exit()