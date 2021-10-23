A, B = map(int, input().split())
biA = format(A, 'b')
biB = format(B, 'b')

box = {"1": "0", "0": "1"}

for i in range(len(biA), max(len(biA), len(biB))):
    biA = '0' + biA

for i in range(len(biB), max(len(biA), len(biB))):
    biB = '0' + biB

biC = ''

for i in range(len(biA)):
    if biB[i] == "1":
        biC += box[biA[i]]
    else:
        biC += biA[i]

print(int(biC, 2))
