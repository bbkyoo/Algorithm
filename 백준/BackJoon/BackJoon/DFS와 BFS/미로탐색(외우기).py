from collections import deque

# dx[0], dy[0] => 오른쪽
# dx[1], dy[1] => 왼쪽
# dx[2], dy[2] => 아래
# dx[3], dy[3] => 위
def bfs(a, b):
    q = deque([])
    q.append((a,b))
    visited[a][b] = 1
    dist[a][b] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and mirro[nx][ny] == 1:
                    q.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1
                    visited[nx][ny] = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())

mirro = [list(map(int ,input())) for _ in range(n)]

visited = [[0]*m for _ in range(n)]
dist = [[0]*m for _ in range(n)]
bfs(0,0)

print(dist[n-1][m-1])











