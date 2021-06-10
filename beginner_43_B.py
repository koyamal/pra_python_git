s = input()

output = ''
for i in s:
    if i == '0':
        output += '0'
    elif i == '1':
        output += '1'
    else:
        output = output[:-1]

print(output)