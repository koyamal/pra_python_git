N = int(input())
s = {}
for i in range(N):
    temp = input()
    if temp not in s:
        s[temp] = 1
    else:
        s[temp] += 1

M = int(input())
t = {}
for i in range(M):
    temp = input()
    if temp not in t:
        t[temp] = 1
    else:
        t[temp] += 1

diff = [0]
for key in s.keys():
    if key in t.keys():
        diff.append(max(0, s[key] - t[key]))
    else:
        diff.append(s[key])

print(max(diff))
