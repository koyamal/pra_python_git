N = int(input())
ss = []
tt = []
for _ in range(N):
    s, t = input().split()
    ss.append(s)
    tt.append(t)

for i in range(N):
    count = 0
    for j in range(N):
        if i != j:
            if ss[i] == ss[j] or ss[i] == tt[j]:
                count += 1
                if count == 2:
                    print("No")
                    exit()
            if tt[i] == ss[j] or tt[i] == tt[j]:
                count += 1
                if count == 2:
                    print("No")
                    exit()

print("Yes")
