N = int(input())

results = ["AC", "WA", "TLE", "RE"]
outputs = [0, 0, 0, 0]

for _ in range(N):
    s = input()
    for i in range(len(results)):
        if s == results[i]:
            outputs[i] += 1

for i in range(len(results)):
    print(results[i], "x", outputs[i])
