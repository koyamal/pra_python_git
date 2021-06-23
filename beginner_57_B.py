N, M = map(int, input().split())
ab_s = []
cd_s = []

for i in range(N):
    ab_s.append(list(map(int, input().split())))

for i in range(M):
    cd_s.append(list(map(int, input().split())))

for ab in ab_s:
    dMin = 0
    indexMin = 0
    for i, cd in enumerate(cd_s):
        if i == 0:
            dMin = abs(ab[0] - cd[0]) + abs(ab[1] - cd[1])
            indexMin = 0

        if abs(ab[0] - cd[0]) + abs(ab[1] - cd[1]) < dMin:
            dMin = abs(ab[0] - cd[0]) + abs(ab[1] - cd[1])
            indexMin = i

    print(indexMin + 1)
