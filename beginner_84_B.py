A, B = map(int, input().split())
S = input()

for i in range(A):
    if S[i] == '-':
        print('No')
        exit()

if S[A] != '-':
    print('No')
    exit()

for i in range(B):
    if S[A + 1 + i] == '-':
        print('No')
        exit()

print('Yes')
