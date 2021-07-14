N = input()

Fx = 0
for i in N:
    Fx += int(i)
if int(N) % Fx == 0:
    print('Yes')
else:
    print('No')
