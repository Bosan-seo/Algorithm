# 백준 2010번

# 내가 작성한 코드

import sys
n = int(input()) # 멀티탭의 개수 N
i = 1
s = 0 # 멀티탭의 개수

while i <= n:
    tmp = int(sys.stdin.readline())
    i += 1
    if i > n:
        s += tmp
    else:
        s += tmp - 1

print(s)

# 다른 사람이 작성한 코드

import sys

input = sys.stdin.readline

N = int(input())
total = 0
for _ in range(N):
    total += int(input())

print(total - N - 1)