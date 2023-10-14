# 백준_8393번
# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

n = int(input())
total = 0
for i in range(1, n+1):
    total += i
print(total)

# chatgpt가 제시한 파이토닉 코드
# n = int(input())
# total = sum(range(1, n+1))
# print(total)
