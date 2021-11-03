Ps = list(map(int, input().split()))

output = ""
for i in range(len(Ps)):
    output += chr(97 + Ps[i] - 1)

print(output)
