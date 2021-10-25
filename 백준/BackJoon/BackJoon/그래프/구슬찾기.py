#from collections import deque

#def heavy_bfs(v):
#    global total_cnt
#    q = deque()
#    q.append(v)
#    visited = [0]*(n+1)
#    visited[v] = 1
#    cnt = 0

#    while q:
#        v = q.popleft()
#        for i in heavy_info[v]:
#            if visited[i] == 0:
#                visited[i] = 1
#                cnt += 1
#                if cnt > standard:
#                    total_cnt += 1
#                    return
#                q.append(i)

#def light_bfs(v):
#    global total_cnt
#    q = deque()
#    q.append(v)
#    visited = [0]*(n+1)
#    visited[v] = 1
#    cnt = 0

#    while q:
#        v = q.popleft()
#        for i in light_info[v]:
#            if visited[i] == 0:
#                visited[i] = 1
#                cnt += 1
#                if cnt > standard:
#                    total_cnt += 1
#                    return
#                q.append(i)

#n, m = map(int, input().split())

#heavy_info = [[] for _ in range(n+1)]
#light_info = [[] for _ in range(n+1)]
#standard = n//2
#total_cnt = 0

#for _ in range(m):
#    a, b = map(int, input().split())
#    heavy_info[b].append(a)
#    light_info[a].append(b)

#for i in range(1, n+1):
#    heavy_bfs(i)
#    light_bfs(i)

#print(total_cnt)

import sys
inf = sys.maxsize

n, m = map(int, input().split())

s = [[0]*n for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    s[a-1][b-1] = 1
    
for k in range(n):
    for i in range(n):
        for j in range(n):
            if s[i][k] and s[k][j]:
                s[i][j] = 1


# 이 부분이 제일 중요 꼭 생각!!!!!!!!!!!!!!!
result = 0
for i in range(len(s)):
    cnt = 0
    rcnt = 0
    for j in range(len(s[i])):
        if s[i][j] == 1:
            cnt += 1
        if s[j][i] == 1:
            rcnt += 1

    if cnt >= n//2 or rcnt >= n//2:
        result += 1

print(result)