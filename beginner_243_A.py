V, A, B, C = map(int, input().split())

while True:
    if V - A < 0:
        print("F")
        exit()

    V -= A

    if V - B < 0:
        print("M")
        exit()

    V -= B

    if V - C < 0:
        print("T")
        exit()

    V -= C
