# 숫자를 입력하면 별이 입력됨
# 공백 규칙이 존재 = 총 줄의 수 - 현재 줄의 번호

n = int(input())

for i in range(1, n+1):
    print(" " * (n-i) + "*" * i)