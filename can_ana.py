with open('/Users/koki/Downloads/dump.log') as f:
    for line in f:
        line = line.split(' ')
        id = line[2].split('#')[0]
        if id == "244":
            data = line[2].split('#')[1]
            f = open('/Users/koki/Downloads/dump.out.log3', 'a')
            f.write(data)
            f.close()
