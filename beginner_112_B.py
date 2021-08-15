N, T = map(int, input().split())

minC = 1001

for i in range(N):
    ci, ti = map(int, input().split())
    if ti <= T:
        if ci <= minC:
            minC = ci

if minC == 1001:
    print("TLE")
else:
    print(minC)
