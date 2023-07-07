# 백준 5532번
# 각각 L, B, A, C, D를 정수로 받음

L = int(input()) # 방학일수

A = int(input()) # 국어 분량

B = int(input()) # 수학 분량

C = int(input()) # 하루 국어 할당량

D = int(input()) # 하루 수학 할당량


if B % D == 0:
    bd = B // D
else:
    bd = B // D + 1
if A % C == 0:
    ac = A//C
else:
    ac = A//C + 1
print(L - max(bd, ac))
