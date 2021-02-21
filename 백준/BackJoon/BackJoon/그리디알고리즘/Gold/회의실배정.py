# 힌트) 정렬을 하면 겹치지 않는 문제다
# 정렬을 1. 끝나는 시간의 오름차순 2. 시작하는 시간의 오름차순
# 출처: https://suri78.tistory.com/26 [공부노트]

import sys

N = int(sys.stdin.readline())

tm = []
for i in range(N):
    w, v = map(int, sys.stdin.readline().split())
    tm.append([w,v])
    
tm.sort(key = lambda x: (x[1], x[0]))

result = 1
end_time = tm[0][1]

for i in range(1,N):
    if tm[i][0] >= end_time:
        result += 1
        end_time = tm[i][1]

print(result)


