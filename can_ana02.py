import codecs

print("start")

with open('/Users/koki/Downloads/dump.out.log3') as f:
    for line in f:
        for i in range(int(len(line) / 2)):
            try:
                print("In try process")
                strData = str(line[2 * i]) + str(line[2 * i + 1])
                print("After Add Data")
                if strData != '00':
                    d = [1, 2]
                    a = [3, 4]
                    t = [5, 6]
                    a = [7, 8]
                    data = str(codecs.decode(strData, 'hex'), 'utf-8')
                    print(data)
            except ValueError as e:
                pass

print("End")