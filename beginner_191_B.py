N, X = map(int, input().split())

As = list(map(int, input().split()))

for A in As:
    if A != X:
        print(A, "", end="")
