n = int(input())

tm = list(map(int, input().split()))

tm.sort()
tm_lt = [tm[0]]
for i in range(1,n):
    tm_lt.append(tm_lt[i-1] + tm[i])

print(sum(tm_lt))