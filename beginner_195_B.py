A, B, W = map(int, input().split())

W = 1000 * W

minNum = 0
maxNum = 0
flagUnsat = True
if W % B == 0:
    minNum = W // B
else:
    num = 1 + W // B
    over = B * num - W
    if B - A > over / num:
        minNum = num
    else:
        flagUnsat = False

if W % A == 0:
    maxNum = W // A
else:
    num = W // A
    lost = W - num * A
    if B - A > lost / num:
        maxNum = num
    else:
        flagUnsat = False

if flagUnsat:
    print(minNum, maxNum)
else:
    print("UNSATISFIABLE")
