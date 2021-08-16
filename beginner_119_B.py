N = int(input())

output = 0
for i in range(N):
    x, u = input().split()
    if u == "JPY":
        output += int(x)
    else:
        output += (float(x) * 380000.0)

print(output)
