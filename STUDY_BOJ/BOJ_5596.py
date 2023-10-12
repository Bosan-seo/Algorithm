# 백준 5596번

slist = list(map(int, input().split()))

tlist = list(map(int, input().split()))
S = 0
T = 0
for i in slist:
    S += i

for j in tlist:
    T += j

if S == T:
    print(S)
else:
    print(max(S,T))