x = [[1, 2, 3], [4, 5, 6]]

y = x.copy()

print("x:", x)
print(id(x[0]))
print("y:", y)
print(id(y[0]))

y[0][1] = 9

print("x:", x)
print(id(x[0]))
print("y:", y)
print(id(y[0]))

y[0] = [7, 8, 9]

print("x:", x)
print(id(x[0]))
print("y:", y)
print(id(y[0]))
