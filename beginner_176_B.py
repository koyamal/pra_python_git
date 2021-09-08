N = input()
sumN = 0

for n in N:
    sumN += int(n)
if sumN % 9 == 0:
    print("Yes")
else:
    print("No")
