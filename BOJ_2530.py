# 백준 2530번

H, M, S = map(int, input().split())

D = int(input())

S += D
M += S//60
H += M//60

print(H%24, M%60, S%60)