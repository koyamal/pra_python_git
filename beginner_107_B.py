H, W = map(int, input().split())

As = []
for i in range(H):
    s = input()
    if "#" in s:
        As.append(s)

whiteIntersect = set(i for i in range(len(As[0])))
for A in As:
    whiteSet = set()
    for i, s in enumerate(A):
        if s == ".":
            whiteSet.add(i)
    whiteIntersect = whiteIntersect & whiteSet

for A in As:
    output = ""
    for i, s in enumerate(A):
        if i not in whiteIntersect:
            output += s
    print(output)
