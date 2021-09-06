S = input()

pS = None
count = 0
output = 0
for i in range(len(S)):
    if pS == S[i] == "R":
        count += 1
    elif (pS is None and S[i] == "R") or (pS == "S" and S[i] == "R"):
        count = 1
    else:
        count = 0
    if count > output:
        output = count
    pS = S[i]

print(output)
