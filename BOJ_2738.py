# 백준_2738번
# N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.

# N과 M을 입력 받기
N, M = map(int, input().split())

# 행렬 A와 B를 입력 받기
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

# 두 행렬을 더해 새로운 행렬 C를 만들기
C = [[A[i][j] + B[i][j] for j in range(M)] for i in range(N)]

# 결과 행렬 C를 출력하기
for row in C:
    print(*row)
