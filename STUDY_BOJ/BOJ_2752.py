# 백준 2752번
# 숫자 세 개를 입력받은 후, 크기를 비교해 오름차순으로 정렬하기

#숫자 세 개 입력받기
numbers = list(map(int,input().split()))

# 숫자 비교하기
numbers.sort()

print(numbers[0], numbers[1], numbers[2])
