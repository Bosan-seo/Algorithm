# 백준 2845번
# 입력을 두번 받음 1째 줄에 1M^2당 몇 명이 있었는지 , 2째 줄엔 각 기사에 실려 있는 참가자수

s, m = map(int,input().split())
news = list(map(int,input().split()))
attended = s * m

# for i in range(len(news)):
#     print(news[i]-attended, end = " ")
# 대신
for i in news:
    print(i - attended, end = " ")

