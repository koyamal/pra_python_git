a = [1, 3, 6, 8, 10, 13, 15, 18, 19, 23, 26, 28, 36, 38, 42]

key = int(input("Input Search Number： "))


def b_search(a, key):
    ps = 0
    pg = len(a) - 1
    pm = (ps + pg) // 2

    while True:
        if a[pm] == key:
            return pm
        elif a[pm] > key:
            pg = pm - 1
        else:
            ps = pm + 1
        pm = (ps + pg) // 2

        if ps > pg:
            return -1


idx = b_search(a, key)
if idx == -1:
    print("Not Exist")
else:
    print("index:", idx)
