X = int(input())

output = 1
nowMoney = 100

while nowMoney < X:
    nowMoney = int(nowMoney * 1.01)
    output += 1

print(output - 1)
