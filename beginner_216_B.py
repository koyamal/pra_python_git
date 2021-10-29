N = int(input())
ST = set()
for _ in range(N):
    ST.add(input())

if N == len(ST):
    print("No")
else:
    print("Yes")
