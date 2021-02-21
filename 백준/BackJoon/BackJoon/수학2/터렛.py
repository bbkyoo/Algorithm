import math

T = int(input())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    count = 0
    d = (x1-x2)**2 + (y1-y2)**2 # 이 문제의 키 포인트는 루트를 씌우지 않고 실수로 만들지 않는 것
    if (r2-r1)**2 < d and d < (r1 + r2)**2: # 원이 두 점에서 만나는 경우
        count = 2
    elif d == (r1 + r2)**2: # 두 원이 외접하는경우(한점에서 만난다)
        count = 1
    elif d == (r2 - r1)**2 and d != 0: # 두 원이 내접하는 경우(한점에서 만난다)
        count = 1
    elif d < (r2 - r1)**2: # 하나의 원이 다른 원을 포함하는 경우(만나지 않는다)
        count = 0
    elif d > (r1 + r2)**2: # 두 원이 멀리 떨어져 만나지 않는 경우
        count = 0
    else: # 두 원이 일치하는 경우(무수히 많은 점에서 만난다)
        count = -1 
    print(count)
