N, M = map(int, input().split())

As = list(map(int, input().split()))
Bs = list(map(int, input().split()))

for b in Bs:
    for i in range(len(As)):
        if b == As[i]:
            As.pop(i)
            break
        if i == len(As) - 1:
            print("No")
            exit()

print("Yes")
