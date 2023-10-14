# 백준_10872번
# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

def factorial():
    N = int(input())
    result = 1
    for i in range(1, N + 1):
        result = result * i
    return result

print(factorial())
