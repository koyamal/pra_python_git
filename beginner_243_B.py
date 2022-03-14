N = int(input())
As = list(map(int, input().split()))
Bs = list(map(int, input().split()))

count_01 = 0
count_02 = 0
for i in range(len(As)):
    if As[i] == Bs[i]:
        count_01 += 1

    if As[i] in Bs:
        count_02 += 1

print(count_01)
print(count_02 - count_01)
