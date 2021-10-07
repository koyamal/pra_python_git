N = int(input())

first = 0
second = 0
Sfirst = ""
Ssecond = ""
for _ in range(N):
    s, t = input().split()
    t = int(t)
    if first < t:
        second, first = first, t
        Ssecond, Sfirst = Sfirst, s
    elif second < t:
        second = t
        Ssecond = s

print(Ssecond)
