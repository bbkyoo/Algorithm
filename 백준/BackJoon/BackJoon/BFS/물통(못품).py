# 각각 부피가 A, B, C(1≤A, B, C≤200) 리터인 세 개의 물통이 있다. 

from collections import deque

def bfs():
    q = deque()
    q.append([0, 0, c])
    while q:
        x, y, z = q.popleft()
        if check[x][y] == 1:
            continue
        check[x][y] = 1

        if x == 0: 
            ans[z] = 1
        if x + y > b:
            q.append([x+y-b, b, z])








a, b, c = map(int, input().split())

check = [[0] * 201 for i in range(201)]
ans = [0 for i in range(201)]
