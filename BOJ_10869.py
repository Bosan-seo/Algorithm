# 백준 10869번
# 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 

def PSMD():
    a, b = map(int,input().split())

    print(a + b)
    print(a - b)
    print(a * b)
    print(a // b)
    print(a % b)
PSMD()