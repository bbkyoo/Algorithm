from collections import deque
import sys

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1

    while q:
        x, y = q.popleft() 

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < m and 0 <= ny < n:
                if visited[nx][ny] == 0 and matrix[nx][ny] == 0:
                    q.append([nx, ny])
                    visited[nx][ny] = 1


m, n = map(int, input().split())

matrix = [list(map(int, input())) for _ in range(m)]
visited = [[0]*n for _ in range(m)]

for i in range(n):
    if visited[0][i] == 0 and matrix[0][i] == 0:
        bfs(0,i)

if 1 in visited[m-1]:
    print("YES")
else:
    print("NO")