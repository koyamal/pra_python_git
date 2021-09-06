S = input()

pS = S[0]
count = 0
output = 0
for i in range(1, len(S)):
    if pS == S[i] == "R":
        count += 1
    else:
        count = 0
    if count > output:
        output = count
    pS = S[i]

if output == 0:
    print(output)
else:
    print(output + 1)
