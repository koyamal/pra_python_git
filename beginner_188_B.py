input()
As = list(map(int, input().split()))
Bs = list(map(int, input().split()))

output = 0
for A, B in zip(As, Bs):
    output += A * B

if output == 0:
    print("Yes")
else:
    print("No")
