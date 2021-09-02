A, B, C, D = map(int, input().split())

numAttach01 = 0
if C % B == 0:
    numAttach01 = C // B
else:
    numAttach01 = 1 + C // B

numAttach02 = 0
if A % D == 0:
    numAttach02 = A // D
else:
    numAttach02 = 1 + A // D

if numAttach01 <= numAttach02:
    print("Yes")
else:
    print("No")
