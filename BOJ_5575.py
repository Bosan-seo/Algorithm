# 백준 5575번
# 직원은 3명

for i in range(3):
    h1, m1, s1, h2, m2, s2 = map(int,input().split())

    start = h1 * 3600 + m1 * 60 + s1

    end = h2 * 3600 + m2 * 60 + s2 

    gap = end - start

    h = gap // 3600
    m = (gap % 3600) // 60
    s = (gap % 3600) % 60

    print(h,m,s)