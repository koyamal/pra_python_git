N, X = map(int, input().split())
As = list(map(int, input().split()))

num_even = N // 2

if sum(As) - num_even <= X:
    print("Yes")
else:
    print("No")
