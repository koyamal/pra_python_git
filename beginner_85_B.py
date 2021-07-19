N = int(input())

dlist = []

for i in range(N):
    dlist.append(int(input()))

print(len(list(set(dlist))))
