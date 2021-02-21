import sys 
from collections import deque 

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input()
    n = int(input())
    de = input().rstrip()[1:-1].split(',') # [1,2,3,4] 이렇게 입력하는 것이 가능해짐
    
    p = p.replace("RR","")
    r = 0
    f, b = 0, 0

    for i in p:
        if i == "R":
            r += 1
        elif i == "D":
            if r % 2 == 0: # r이 짝수이면 앞에서 부터 빼야하므로 f에 +1
                f += 1
            else:          # r이 홀수이면 뒤에서 부터 빼야하므로 b에 +1
                b += 1

    if f + b <= n: 
        de = de[f: n-b] # 앞에서 부터 빼야하는 것과 뒤에서 부터 빼야하는 것을 자른다.

        if r % 2 == 1: # r 이 홀수이면 뒤집어서 출력 
            print('[' + ','.join(de[::-1])+']')
        else:          # r 이 짝수이면 그데로 출력
            print('[' + ','.join(de)+']')
    else:
        print('error')