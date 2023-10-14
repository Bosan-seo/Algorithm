# 백준 1252번
# 이진수 두개를 입력받아 더하기

a, b = map(lambda x: int(x,2), input().split())

s = a + b

print(bin(s)[2:])