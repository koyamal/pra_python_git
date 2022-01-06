N = int(input())

if N >= 42:
    N += 1

lenN = len(str(N))
output = ""
for _ in range(3 - lenN):
    output += "0"

print("AGC" + output + str(N))
