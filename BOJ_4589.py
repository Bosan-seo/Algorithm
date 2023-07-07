# 백준 4589번
# 세 가지 숫자를 입력받음 -> 숫자가 오름차순이나 내림차순으로 입력됐을 경우 ORDERED, 아니면 UNORDERED가 출력

num = int(input())
x = []

for i in range(num):
    x.append(list(map(int,input().split())))

print("Gnomes:")

for i in x:
    if i == sorted(i) or i == sorted(i, reverse = True):
        print("Ordered")
    else:
        print("Unordered")
