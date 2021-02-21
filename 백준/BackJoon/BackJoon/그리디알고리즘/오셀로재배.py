import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    init = list(map(str, input().strip()))
    target = list(map(str, input().strip()))

    r1 = 0
    r2 = 0
    for i in range(n):
        if init[i] == 'W' and target[i] == 'B':
            r1 += 1
        elif init[i] == 'B' and target[i] == 'W':
            r2 += 1
        
    if r1 < r2:
        print(r2)
    else:
        print(r1)

    
