# 백준_15964번
# A＠B = (A+B)×(A-B)

def calc(a, b):
    result = (a + b) * (a - b)
    return result

a, b = map(int,input().split())
print(calc(a, b))
