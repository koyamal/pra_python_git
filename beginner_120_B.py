A, B, K = map(int, input().split())

numCount = 0

for i in range(min(A, B)):
    if A % (min(A, B) - i) == 0 and B % (min(A, B) - i) == 0:
        numCount += 1
        if numCount == K:
            print(min(A, B) - i)
            exit()
