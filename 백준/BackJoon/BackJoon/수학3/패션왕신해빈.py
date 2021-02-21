# (옷 종류 + 1)(옷 종류 +1) - 1 = 결과

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    
    wear = []
    for i in range(n):
        wear.append(sys.stdin.readline().split()[1]) # 이 부분이 중요

    set_wear = tuple(set(wear)) # 이 부분도
    
    type = []
    for i in range(len(set_wear)):
        type.append(wear.count(set_wear[i]))

    result = 1
    for t in type:
        result *= (t + 1)

    print(result - 1)