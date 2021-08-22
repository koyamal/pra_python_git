A, B = map(int, input().split())

ave = (A + B) / 2
if ave.is_integer():
    print(int(ave))
else:
    print("IMPOSSIBLE")
    