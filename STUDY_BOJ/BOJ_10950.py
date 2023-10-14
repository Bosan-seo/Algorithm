# 백준_10950번
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

t = int(input())  # 테스트 케이스 개수 t를 입력받음

for _ in range(t):  # t 만큼 반복
    a,b = map(int,input().split())
    print(a+b)