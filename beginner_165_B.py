X = int(input())

output = 1
nowMoney = 100

while nowMoney < X:
    #nowMoney = int(nowMoney * 1.01)
    #nowMoney += int(nowMoney * 0.01)
    nowMoney += nowMoney // 100
    output += 1

print(output - 1)
