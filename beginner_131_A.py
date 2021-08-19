S = input()

preS = ""
for s in S:
    if s == preS:
        print("Bad")
        exit()
    preS = s
print("Good")
