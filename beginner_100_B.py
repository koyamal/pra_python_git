D, N = map(int, input().split())

startNumber = 100 ** D
print(startNumber * N + startNumber * (startNumber * N // (100 ** (D + 1))))