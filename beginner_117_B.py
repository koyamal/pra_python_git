N = int(input())

listL = list(map(int, input().split()))

if max(listL) < sum(listL) - max(listL):
    print("Yes")
else:
    print("No")
