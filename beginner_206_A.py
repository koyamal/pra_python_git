N = int(input())

price = 1.08 * N

if price < 206:
    print("Yay!")
elif price < 207:
    print("so-so")
else:
    print(":(")
