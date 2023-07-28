# 백준 1076번
# 만약 0, 1 칸에 들어간다면 값을 쓰고, 2칸에 들어간다면 곱을 쓴다.

resistor_dict = {
    "black": [0, 1],
    "brown": [1, 10],
    "red": [2, 100],
    "orange": [3, 1000],
    "yellow": [4, 10000],
    "green": [5, 100000],
    "blue": [6, 1000000],
    "violet": [7, 10000000],
    "grey": [8, 100000000],
    "white": [9, 1000000000]
}

color1 = input()
color2 = input()
color3 = input()

if color1 in resistor_dict:
    color1 = resistor_dict[color1][0]

if color2 in resistor_dict:
    color2 = resistor_dict[color2][0]

if color3 in resistor_dict:
    color3 = resistor_dict[color3][1]

tmp = str(color1) + str(color2)

print(int(tmp)* int(color3))