#백준 2480번 문제
# 정수 3개를 받음 -> 같은 눈이 나온 상황에 따라 다른 계산이 필요

a, b, c = map(int,input().split())

if a == b == c:
    print(10000 + a * 1000)
elif a == b or b == c:
    print(1000 + b * 100)
elif a == c:
    print(1000 + a * 100)
else:
    print(100 * max(a, b, c))

# gpt 개선코드
# a, b, c = map(int,input().split())

# if a == b == c:
#     prize = 10000 + a * 1000
# elif a == b or a == c or b == c:
#     prize = 1000 + (a if a == b or a == c else b) * 100
# else:
#     prize = 100 * max(a, b, c)

# print(prize)
