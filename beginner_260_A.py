S = input()


def counter(s, S):
    output = 0
    for i in range(len(S)):
        if s == S[i]:
            output += 1
    return output


for i in range(len(S)):
    if counter(S[i], S) == 1:
        print(S[i])
        exit()

print(-1)
