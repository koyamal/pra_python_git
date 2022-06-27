N, X = map(int, input().split())
box = ''
for i in range(ord('A'), ord('Z') + 1):
    box += chr(i) * N
print(box[X - 1])
