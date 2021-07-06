from collections import deque

dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,-1,1,1,-1]

def bfs(x, y):
    q = deque([])
    q.append([x, y])
    visited[x][y] = 1

    while q:
        x, y = q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if visited[nx][ny] == 0 and matrix[nx][ny] == 1:
                    q.append([nx, ny])
                    visited[nx][ny] = 1

m, n = map(int, input().split())

matrix = []
for _ in range(m):
    matrix.append(list(map(int, input().split())))

visited = [[0]*n for _ in range(m)] 

answer = 0
for i in range(m):
    for j in range(n):
        if matrix[i][j] == 1 and visited[i][j] == 0:
            bfs(i, j)
            answer += 1

print(answer)




