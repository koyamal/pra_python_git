X = int(input())

num500 = X // 500
num5 = (X - 500 * num500) // 5

print(1000 * num500 + 5 * num5)
