K = int(input())
A, B = input().split()

lenA = len(A)
lenB = len(B)
tenA = 0
tenB = 0

for i in range(lenA):
    tenA += int(A[i]) * (K ** (lenA - i - 1))

for i in range(lenB):
    tenB += int(B[i]) * (K ** (lenB - i - 1))

print(tenA * tenB)
