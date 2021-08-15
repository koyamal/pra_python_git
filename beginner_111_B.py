N = input()

if int(N) <= 111 * int(N[0]):
    print(111 * int(N[0]))
else:
    print(111 * (int(N[0]) + 1))
