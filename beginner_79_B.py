N = int(input())


def cal_L(target, result):
    if target == 0:
        return 2
    if target == 1:
        return 1

    if target - 1 not in result:
        result[target - 1] = cal_L(target - 1, result)

    if target - 2 not in result:
        result[target - 2] = cal_L(target - 2, result)

    return result[target - 1] + result[target - 2]


result_L = {0: 2, 1: 1}

if N == 1:
    print('1')
else:
    print(cal_L(N, result_L))
