from collections import deque

def bfs():  
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q = deque([])
    q.append([0,0])
    visited[0][0] = 1 

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                
                if matrix[nx][ny] == 0:
                    q.appendleft([nx, ny])
                    visited[nx][ny] = visited[x][y]

                elif matrix[nx][ny] == 1:
                    q.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1

m, n = map(int, input().split())

matrix = []
visited = [[0]*m for _ in range(n)]
for _ in range(n):
    matrix.append(list(map(int, input())))

bfs()
print(visited[n-1][m-1] - 1)