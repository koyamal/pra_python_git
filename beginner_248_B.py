A, B, K = map(int, input().split())

now = A
count = 0
while True:
    if now >= B:
        print(count)
        exit()
    count += 1
    now = A * (K ** count)
