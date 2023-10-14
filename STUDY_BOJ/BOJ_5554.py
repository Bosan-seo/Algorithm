#백준 5554번
#기록이 전부 초단위로 입력
A = int(input())
B = int(input())
C = int(input())
D = int(input())

S = A + B + C + D
M = S//60

print(M)
print(S%60)