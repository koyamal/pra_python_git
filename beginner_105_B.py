N = int(input())

multipulesOf7 = [i * 7 for i in range(15)]
multipulesOf4 = [i * 4 for i in range(26)]

for multipuleOf7 in multipulesOf7:
    diff = N - multipuleOf7
    if diff in multipulesOf4:
        print("Yes")
        exit()

print("No")
