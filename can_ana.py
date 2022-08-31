path = '/Users/koki/Downloads/'
with open(path + 'dump.log') as f:
    for line in f:
        line = line.split(' ')
        nid = line[2].split('#')
        if nid[0] == "244":
            data = nid[1]
            fw = open(path + 'dump.out.log3', 'a')
            fw.write(data)
            fw.close()
