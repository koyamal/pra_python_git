L1, R1, L2, R2 = map(int, input().split())
s1 = set(range(L1, R1 + 1))
s2 = set(range(L2, R2 + 1))
print(max(0, len(s1 & s2) - 1))
