# 데스 나이트가 있는 곳이 (r, c)라면, (r-2, c-1), (r-2, c+1), (r, c-2), (r, c+2), (r+2, c-1), (r+2, c+1)로 이동할 수 있다.
# (r1, c1)에서 (r2, c2)로 이동하는 최소 이동 횟수

from collections import deque
import sys

input = sys.stdin.readline

dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    dist[x][y] = 0
    while q:
        x, y = q.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 :
                    q.append([nx, ny])
                    visited[nx][ny] = 1
                    dist[nx][ny] = dist[x][y] + 1
                     
n = int(input())

matrix = [[0]*n for _ in range(n)]
visited = [[0]*n for _ in range(n)]
dist = [[0]*n for _ in range(n)]

r1, c1, r2, c2 = map(int, input().split())
matrix[r1][c1] = 1
matrix[r2][c2] = 2

bfs(r1,c1)

if dist[r2][c2] == 0:
    print(-1)
else:
    print(dist[r2][c2])






