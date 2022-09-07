N = int(input())
As = []
for _ in range(N):
    As.append(input())

for i in range(N):
    for j in range(N):
        if As[i][j] == '-':
            if As[j][i] != '-':
                print('incorrect')
                exit()
        if As[i][j] == 'W':
            if As[j][i] != 'L':
                print('incorrect')
                exit()
        if As[i][j] == 'D':
            if As[j][i] != 'D':
                print('incorrect')
                exit()
        if As[i][j] == 'L':
            if As[j][i] != 'W':
                print('incorrect')
                exit()

print('correct')
