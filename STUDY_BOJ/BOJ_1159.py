# 백준 1159번
# 선수의 수 입력 다음부터 선수 이름 입력

n = int(input())

fst_letters = []

for _ in range(n):
    name = input()
    fst_letters.append(name[0])

letter_count = {}

for letter in fst_letters:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1

selected_letters = []

for letter, count in letter_count.items():
    if count >= 5:
        selected_letters.append(letter)

if len(selected_letters) > 0:

    sorted_letters = sorted(selected_letters)

    for letter in sorted_letters:
        print(letter, end = "")
else:
    print("PREDAJA")