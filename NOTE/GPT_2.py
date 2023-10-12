# 팰린드롬 체크

def is_pallindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

s = input("문자열을 입력해주세요: ")

print(is_pallindrome(s))