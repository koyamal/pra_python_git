N = input()
Ws = list(map(int, input().split()))

sumW = sum(Ws)

sumWi = 0

for W in Ws:
    sumWi += W
    if sumWi >= sumW / 2:
        print(min(int(2 * abs(sumWi - (sumW / 2))), int(2 * abs((sumW / 2) - (sumWi - W)))))
        exit()
