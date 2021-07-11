N = int(input())
K = int(input())

output = 1

for i in range(N):
    output = min(output * 2, output + K)

print(output)
