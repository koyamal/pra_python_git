N = int(input())
P = list(map(int, input().split()))

count = 1
s = N
while True:
    if P[s - 2] == 1:
        print(count)
        exit()
    s = P[s - 2]
    count += 1
