N = int(input())
S = input()

AtoZ = [chr(i) for i in range(65, 65+26)]

output = ""
for s in S:
    if AtoZ.index(s) + N >= len(AtoZ):
        output += AtoZ[AtoZ.index(s) + (N % 26) - len(AtoZ)]
    else:
        output += AtoZ[AtoZ.index(s) + (N % 26)]

print(output)
