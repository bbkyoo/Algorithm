from collections import deque
import sys

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(start):
    q = deque([start])
    
    while q:
        x, y, wall = q.popleft()
        dist = visited[x][y][wall] + 1

        if [x, y] == [n-1, m-1]:
            return visited[x][y][wall]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny][wall] == 0:
                if matrix[nx][ny] == 0:
                    visited[nx][ny][wall] = dist
                    q.append([nx, ny, wall])
                elif wall < k:
                    visited[nx][ny][wall + 1] = dist
                    q.append([nx, ny, wall+1])

    return -1

n, m, k = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().strip())))

visited = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]
visited[0][0] = [1]*(k+1)
print(bfs((0,0,0)))