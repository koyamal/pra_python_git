N, L = map(int, input().split())

output = 0
minApple = L
for i in range(N):
    apple = L + i
    output += apple
    if abs(apple) < abs(minApple):
        minApple = apple

print(output - minApple)
