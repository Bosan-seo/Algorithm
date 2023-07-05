# 문자열 받기 -- 모음일 경우 카운팅하기 -- 자음일 경우 패스하기 -- 총 개수 세기

while True:
    sentence = input()
    count = 0
    if sentence == '#':	# 입력의 끝
        break
    for c in sentence:
        if c in 'aeiouAEIOU': # 모음이면
            count += 1
    print(count)