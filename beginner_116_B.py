recentA = int(input())
As = [recentA]


def cal_ai(rA):
    if rA % 2 == 0:
        return int(rA / 2)
    else:
        return (rA * 3) + 1


countIndex = 1
exitFlag = False
while not exitFlag:
    countIndex += 1
    recentA = cal_ai(recentA)
    if recentA in As:
        exitFlag = True
    else:
        As.append(recentA)

print(countIndex)
