N = int(input())
T, A = map(int, input().split())
listH = list(map(int, input().split()))

minDiff = abs(A - (T - 0.006 * listH[0]))
minIndex = 0
for i, H in enumerate(listH):
    if abs(A - (T - 0.006 * H)) < minDiff:
        minDiff = abs(A - (T - 0.006 * H))
        minIndex = i

print(minIndex + 1)
