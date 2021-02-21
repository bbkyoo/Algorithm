# 서류심사 성적을 기준으로 오름차순으로 설정한다.
# 그리고 면접성적만 확인하면서 검사를 해나가는데
# min_n보다 작은 값이 있다면 min_n에 저장해주고
# min_n보다 크다면 cnt를 증가시켜준다.

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    
    list = []
    
    for i in range(N):
        one, two = map(int, input().split())
        list.append([one, two])
    
    list.sort()
    
    min_n = list[0][1]
    count = 0

    for k in range(1, N):
        if min_n < list[k][1]:
            count += 1
        else:
            min_n = list[k][1]
    
    print(N-count)

