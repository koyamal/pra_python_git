input()
As = list(map(int, input().split()))

for A in As:
    if A % 2 == 0:
        if A % 3 != 0 and A % 5 != 0:
            print("DENIED")
            exit()

print("APPROVED")
