S = input()
head = int(S[:2])
tail = int(S[2:])

if 0 < tail < 13:
    if 0 < head < 13:
        print("AMBIGUOUS")
    else:
        print("YYMM")
else:
    if 0 < head < 13:
        print("MMYY")
    else:
        print("NA")


