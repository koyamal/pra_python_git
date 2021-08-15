N, T = map(int, input().split())

minT = 1001

for i in range(N):
    ci, ti = map(int, input().split())
    if ti <= T:
        if ci <= minT:
            minT = ci

if minT == 1001:
    print("TLE")
else:
    print(minT)
