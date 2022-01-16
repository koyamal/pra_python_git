def functionF(x):
    return x * x + 2 * x + 3


t = int(input())


print(functionF(functionF(functionF(t) + t) + functionF(functionF(t))))
