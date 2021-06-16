N = input()
T = list(map(int, input().split()))
M = int(input())

l = []
for m in range(M):
    p, x = map(int, input().split())
    output = 0
    for k, t in enumerate(T):
        if k == p - 1:
            output += x
        else:
            output += t
    l.append(output)

for i in l:
    print(i)






