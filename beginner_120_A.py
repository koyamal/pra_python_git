A, B, C = map(int, input().split())

numSounds = B // A
if numSounds > C:
    print(C)
else:
    print(numSounds)
