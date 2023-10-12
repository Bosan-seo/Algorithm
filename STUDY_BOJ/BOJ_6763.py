#백준 6763번
# 두 수를 입력받음. 제한 속력과 차량 속력 두 수를 비교해 기준에 맞는 출력을 함

limit_speed = int(input())
your_speed = int(input())
exceeded_speed = your_speed - limit_speed

if exceeded_speed <= 0:
    print("Congratulations, you are within the speed limit!")
elif 1 <= exceeded_speed <= 20:
    print("You are speeding and your fine is $100.")
elif 21 <= exceeded_speed <= 30:
    print("You are speeding and your fine is $270.")
else:
    print("You are speeding and your fine is $500.")