import math
T = int(input())

for i in range(T):
    x, y = map(int, input().split())
    len = int(y - x)
    
    if len <= 3:
        print(len)
    else:
        n = int(math.sqrt(len)) #루트 씌우기
        if len == n**2:
            print(2*n-1)
        elif n**2 < len <= n**2+n:
            print(2*n)
        else:
            print(2*n+1)

