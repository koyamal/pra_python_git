input()
Xs = map(int, input().split())

distMan = 0
distEuclid = 0
distCheb = 0

for x in Xs:
    a = abs(x)
    distMan += a
    distEuclid += a * a
    if distCheb < a:
        distCheb = a

print(distMan)
print(distEuclid ** 0.5)
print(distCheb)
