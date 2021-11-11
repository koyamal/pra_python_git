N, P = map(int, input().split())
listA = list(map(int, input().split()))

output = 0

for a in listA:
    if a < P:
        output += 1

print(output)
