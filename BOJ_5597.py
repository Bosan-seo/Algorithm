# 백준_5597번
# X대학 M교수님은 프로그래밍 수업을 맡고 있다. 교실엔 학생이 30명이 있는데, 학생 명부엔 각 학생별로 1번부터 30번까지 출석번호가 붙어 있다.
# 교수님이 내준 특별과제를 28명이 제출했는데, 그 중에서 제출 안 한 학생 2명의 출석번호를 구하는 프로그램을 작성하시오.

num_list = list(range(1,31))
i = 0
submit_list = []
unsubmit = []
while i < 28:
    submit_list.append(int(input()))
    unsubmit = [item for item in num_list if item not in submit_list]    
    i += 1
print(unsubmit[0])
print(unsubmit[1])

# chatgpt가 제시한 최적화된 코드
# 1. 학생 명단 생성
# num_list = list(range(1,31))

# 2. 과제 제출 명단 생성
# submit_list = [int(input()) for _ in range(28)]

# 3. 미제출자 찾기
# unsubmit = [item for item in num_list if item not in submit_list]

# 4. 미제출자 출석번호 출력
# print(unsubmit[0])
# print(unsubmit[1])


# 차이점: 내가 작성한 코드는 불필요한 연산이 많다. for 루프를 사용했다면 더 간결하게 작성할 수 있음.
