K = int(input())
h = K // 60
m = K % 60

ms = '0' + str(m)
print(str(21 + h) + ':' + ms[len(ms) - 2:])
