H, W = map(int, input().split())

listS = []

for i in range(H):
    listS.append(input())


def count_bomb(i_index, j_index, S):
    output = 0
    for i_temp in range(max(0, i_index - 1), min(H, i_index + 2)):
        for j_temp in range(max(0, j_index - 1), min(W, j_index + 2)):
            if S[i_temp][j_temp] == '#':
                output += 1
    return output

for i in range(H):
    output = ''
    for j in range(W):
        if listS[i][j] == '#':
            output += '#'
        else:
            output += str(count_bomb(i, j, listS))
    print(output)
