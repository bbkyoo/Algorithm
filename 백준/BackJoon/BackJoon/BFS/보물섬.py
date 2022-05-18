# 육지(L)나 바다(W)
# 보물은 서로 간에 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀있다.

from collections import deque
import sys

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
    q = deque()
    q.append([x, y])

    visited = [[0] * m for _ in range(n)]
    dist = [[0] * m for _ in range(n)]

    visited[x][y] = 1
    dist[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and mp[nx][ny] == 'L':
                    q.append([nx, ny])
                    visited[nx][ny] = 1
                    dist[nx][ny] = dist[x][y] + 1
    mx = 0
    for i in dist:
        mx = max(mx, max(i))
    return mx

n, m = map(int, input().split())

mp = []
for _ in range(n):
    mp.append(list(input()))

result = 0
for i in range(n):
    for j in range(m):
        if mp[i][j] == 'L':
            result = max(result, bfs(i, j))
            
print(result-1)









