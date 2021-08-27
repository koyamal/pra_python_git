input()
S, T = input().split()

output = ""
for s, t in zip(S, T):
    output += s + t

print(output)
