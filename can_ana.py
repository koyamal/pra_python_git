with open('/Users/koki/Downloads/dump.log') as f:
    for line in f:
        line = line.split(' ')
        nid = line[2].split('#')
        if nid[0] == "244":
            data = nid[1]
            f = open('/Users/koki/Downloads/dump.out.log3', 'a')
            f.write(data)
            f.close()
