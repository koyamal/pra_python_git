N = int(input())
setA = set(map(int, input().split()))

if N == len(setA):
    print("Yes")
else:
    print("No")
