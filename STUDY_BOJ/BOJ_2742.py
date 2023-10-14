# 백준 2742번
#자연수를 받으면 첫째줄에 N... 마지막줄에 1을 출력하도록 만든다

n = int(input())

for i in range(1, n+1):
    print(n-i+1)