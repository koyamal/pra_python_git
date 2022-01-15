L, R = map(int, input().split())
S = input()

mid = ""
for i in range(L, R + 1):
    mid = S[i - 1] + mid

print(S[: L - 1] + mid + S[R: ])
