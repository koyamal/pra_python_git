S = input()

if (not S.islower()) & (not S.isupper()) & (len(set(S)) == len(S)):
    print("Yes")
else:
    print("No")
