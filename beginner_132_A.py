S = input()
setS = set(s for s in S)

if len(setS) == 2:
    listUniqS = list(setS)
    if S.count(listUniqS[0]) == 2:
        print("Yes")
    else:
        print("No")
else:
    print("No")
