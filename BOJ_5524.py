# 백준 5524번
# 첫째 줄에 정수 N을 받고, 둘째 줄에는 문자열을 받는다. -> 정수 N만큼 문자열을 받음 -> 받은 문자열을 모두 소문자로 변환

num = int(input())
for i in range(num):
    user_string = input()
    Si = user_string.lower()
    print(Si)