input()
As = list(map(int, input().split()))

if 0 in As:
    print("0")
    exit()

output = 1

for A in As:
    output *= A
    if output > 10 ** 18:
        print(-1)
        exit()

print(output)
