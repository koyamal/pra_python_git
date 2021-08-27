A, B, K = map(int, input().split())

if K > A:
    print("0 " + str(max(0, A + B - K)))
else:
    print(str(A - K) + " " + str(B))
