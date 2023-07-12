# 백준 6764번
# 4개의 수열을 받고 수열이 점차 증가하는 형태면 fish rising, 감소하는 형태면 fish diving, 일정하면 constant depth, 불규칙적이면 no fish를 출력

a = int(input())
b = int(input())
c = int(input())
d = int(input())

num_list = [a, b, c, d]

if num_list[0] == num_list[1] == num_list[2] == num_list[3]:
    print("Fish At Constant Depth")
elif num_list == sorted(num_list):
    print("Fish Rising")
elif num_list == sorted(num_list, reverse=True):
    print("Fish Diving")
else:
    print("No Fish")