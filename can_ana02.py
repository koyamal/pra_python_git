import codecs
output = ""
with open('/Users/koki/Downloads/dump.out.log3') as f:
    for line in f:
        for i in range(int(len(line) / 2)):
            try:
                if str(line[2 * i]) + str(line[2 * i + 1]) == "00":
                    pass
                else:
                    data = str(codecs.decode(str(line[2 * i]) + str(line[2 * i + 1]), "hex"), 'utf-8')
                    print(data)
                    if output[len(output) - 1:] != data:
                        output = output + data
            except ValueError as e:
                pass

print(output)