A, B = input().split()

maxlen = max(len(A), len(B))

for _ in range(len(A), maxlen):
    A = "0" + A

for _ in range(len(B), maxlen):
    B = "0" + B

for i in range(maxlen):
    if int(A[maxlen - 1 - i]) + int(B[maxlen - 1 - i]) >= 10:
        print("Hard")
        exit()

print("Easy")
