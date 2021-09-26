X = input()

indexDot = X.find(".")

if indexDot == -1:
    print(X)
else:
    print(X[:indexDot])
