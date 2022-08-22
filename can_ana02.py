import numpy
print("66".decode("hex"))
with open('/Users/koki/Downloads/dump.out.log3') as f:
    for line in f:
        for i in range(int(len(line) / 2)):
            try:
                if str(line[2 * i]) + str(line[2 * i + 1]) == "00":
                    pass
                else:
                    print(str(line[2 * i]) + str(line[2 * i + 1]))
                    print(chr(int(str(line[2 * i]) + str(line[2 * i + 1]))))
                    print(chr(hex(66)))
            except ValueError as e:
                pass