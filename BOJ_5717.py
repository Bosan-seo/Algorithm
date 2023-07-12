# 백준 5717번
# 숫자 두개 입력받아 더하기


while True:
    m, f = map(int,input().split())

    if m == 0 and f == 0:
        break
    else:
        print(m + f)
