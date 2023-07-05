# 백준 2440번
# 첫째 줄에 별 N개... N번째 줄에 별 1개를 찍는 문제
# 별 입력 규칙 = N + 1 - i
n = int(input())

for i in range(1, n+1):
    print("*" * (n-i+1))