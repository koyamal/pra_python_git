A, B, C, D, E, F, X = map(int, input().split())

numT = X //(A + C)
remT = X % (A + C)
numA = X // (D + F)
remA = X % (D + F)

#disT = numT * B * A + B * remT
disT = numT * B * A + B * min(remT, A)
#disA = numA * E * D + E * remA
disA = numA * E * D + E * min(remA, D)

if disT > disA:
    print("Takahashi")
elif disT < disA:
    print("Aoki")
else:
    print("Draw")
