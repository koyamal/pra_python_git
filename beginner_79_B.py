N = int(input())

def cal_L(target):
    if target == 0:
        return 2
    if target == 1:
        return 1

    return cal_L(target - 1) + cal_L(target - 2)

if N == 1:
    print('1')
else:
    print(cal_L(N))
