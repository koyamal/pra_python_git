N = int(input())
D, X = map(int, input().split())

count_eta = 0
for i in range(N):
    count_eta += 1
    count_eta += (D - 1) // int(input())

print(count_eta + X)
