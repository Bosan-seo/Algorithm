# 백준_2744번
# 영어 소문자와 대문자로 이루어진 단어를 입력받은 뒤, 대문자는 소문자로, 소문자는 대문자로 바꾸어 출력하는 프로그램을 작성하시오.

# 단어 입력받기
S = list(input())
S2 = []
for i in range(0, len(S)):
    if S[i].isupper():
        S2.append(S[i].lower)
    elif S[i].islower():
        S2.append(S[i].upper)
print(S2)