s = input().strip()


def can_be_palindrome(s):
    if s == s[::-1]:
        return True
    cnt_a = 0
    while cnt_a < len(s) and s[-1 - cnt_a] == "a":
        cnt_a += 1
    cnt_a_start = 0
    while cnt_a_start < len(s) and s[cnt_a_start] == "a":
        cnt_a_start += 1
    middle = s[cnt_a_start : len(s) - cnt_a]
    return cnt_a_start <= cnt_a and middle == middle[::-1]


print("Yes" if can_be_palindrome(s) else "No")
