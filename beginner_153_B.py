H, N = map(int, input().split())
As = list(map(int, input().split()))

if sum(As) >= H:
    print("Yes")
else:
    print("No")
