N = int(input())
ai_b = [1]

for i in range(N):
    ai = []
    for j in range(i + 1):
        if j == 0 or j == i:
            ai.append(1)
        else:
            ai.append(ai_b[j - 1] + ai_b[j])
    output = str(ai[0])
    for j in range(1, i + 1):
        output += " " + str(ai[j])
    print(output)
    ai_b = ai
