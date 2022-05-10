H, W = map(int, input().split())
R, C = map(int, input().split())

output = 4
if R == 1:
    output -= 1

if R == H:
    output -= 1

if C == 1:
    output -= 1

if C == W:
    output -= 1

print(output)
