# 백준 1225번

# A * B의 방식을 새롭게 정의
# A가 a1, a2로 구성되어 있고, B가 b1, b2로 구성되어 있다면
# (a1 * b1) + (a1 * b2) + (a2 * b1) + (a2 * b2)의 형태

a, b = input().split()

a = list(map(int, a))
b = list(map(int, b))
print(sum(a) * sum(b))