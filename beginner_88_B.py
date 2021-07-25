input()

listA = list(map(int, input().split()))
listA.sort(reverse=True)

output = 0

for i, A in enumerate(listA):
    if i % 2 == 0:
        output += A
    else:
        output -= A

print(output)

