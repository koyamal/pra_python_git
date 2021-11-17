N = int(input())

a, b = map(int, input().split())

countA = 1
countB = 1
for _ in range(N - 2):
    tempa, tempb = map(int, input().split())
    if a == tempa or a == tempb:
        countA += 1

    if b == tempa or b == tempb:
        countB += 1

if countA == N - 1 or countB == N - 1:
    print("Yes")
else:
    print("No")
