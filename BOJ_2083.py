#럭비 클럽 회원 분류 
# 분류 기준 --- 나이 or 몸무게 =< 80kg else: 청소년
# 입력받는 데이터 --- name age weight
# 성인부면 senior가 청소년부면 junior가 출력됨
# 마지막줄은 # 0 0

while True:
    name, age, weight = input().split()
    club = 0
    if name == "#" and age == 0 and weight == 0:
        break
    else:
        if int(age) > 17 or int(weight) >= 80:
            club = "Senior"
        else:
            club ="Junior"            
    
    print(f"{name}", club)
