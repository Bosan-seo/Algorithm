# 백준 10430번

a, b, c = map(int, input().split())

print((a + b) % c)
print(((a % c) + (b % c)) % c)
print((a * b) % c)
print((a % c) * (b % c) % c)

# gpt의 개선된 코드

# def perform_operations(a, b, c):
#     print((a + b) % c)
#     print(((a % c) + (b % c)) % c)
#     print((a * b) % c)
#     print(((a % c) * (b % c)) % c)

# # Get input and perform operations
# a, b, c = map(int, input().split())
# perform_operations(a, b, c)
