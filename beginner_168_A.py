N = input()

if N[len(N) - 1] in "3":
    print("bon")
elif N[len(N) - 1] in "0168":
    print("pon")
else:
    print("hon")
