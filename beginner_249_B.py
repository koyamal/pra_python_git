S = input()

if (not S.islower()) & (not S.isupper()) & (len(set(S)) == len(S)):
    print("Yes")
    exit()
else:
    print("No")
    exit()
