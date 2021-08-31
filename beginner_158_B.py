N, A, B = map(int, input().split())

quot = N // (A + B)
remainder = N % (A + B)

print(quot * A + min(remainder, A))
