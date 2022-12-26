import codecs

with open('/Users/koki/Downloads/dump.out.log3') as f:
    for line in f:
        for i in range(int(len(line) / 2)):
            try:
                strData = str(line[2 * i]) + str(line[2 * i + 1])
                if strData != '00':
                    data = str(codecs.decode(strData, 'hex'), 'utf-8')
                    print(data)
            except ValueError as e:
                pass

print("End")