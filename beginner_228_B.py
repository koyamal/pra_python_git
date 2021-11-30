N, X = map(int, input().split())

As = list(map(int, input().split()))
Ks = [X]

index = X - 1
while True:
    if As[index] not in Ks:
        Ks.append(As[index])
        index = As[index] - 1
    else:
        break

print(len(Ks))
