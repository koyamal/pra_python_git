def judge_palindrome(S):
    for i in range(len(S) // 2):
        if S[i] != S[len(S) - 1 - i]:
            return False
    return True


S = input()

if judge_palindrome(S) and judge_palindrome(S[:int(len(S) // 2)]) and judge_palindrome(S[int((len(S) + 2) // 2):]):
    print("Yes")
else:
    print("No")
