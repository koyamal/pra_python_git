S = input()

lengthS = len(S)

for i in range(lengthS):
    S = S[:len(S) - 1]
    if len(S) % 2 == 0:
        if S[:int(len(S)/2)] == S[int(len(S)/2):]:
            print(len(S))
            exit()
