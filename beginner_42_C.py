M, K = input().split()
D = list(map(int, input().split()))
L = [i for i in range(10)]

U = list(set(D) ^ set(L))

output = ""
N = [int(i) for i in list(M)]
for i in range(len(N)):
    flag = False
    for k in U:
        if k >= int(N[len(N) - 1 - i]):
            output = str(k) + output
            flag = True
            break
    if(flag == False):
        N[len(N) - 1 - i - 1] = N[len(N) - 1 - i - 1] + 1
        output = str(U[0]) * (i + 1)

output_int = int(output)

if output_int < int(M):
    if U[0] == 0:
        output = str(U[1]) + output
    else:
        output = str(U[0]) + output

print(output)
