from collections import deque
import sys

inf = sys.maxsize

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(x, y):
    q = deque([])
    q.append([x, y])
    visited[x][y] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            while True:
                if 0 <= nx < h and 0 <= ny < w:
                    # 벽을 만난다.
                    if matrix[nx][ny] == '*':
                        break

                    # 지난 적 있는 곳인데, 지금 경로로는 너무 많은 거울이 필요해서 break
                    if visited[nx][ny] < visited[x][y] + 1:
                        break

                    # matrix 업데이트, q 추가
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                    nx = nx + dx[i]
                    ny = ny + dy[i]
                else:
                    break

w, h = map(int, input().split())

matrix = []
for _ in range(h):
    matrix.append(list(input()))

c = []
for i in range(h):
    for j in range(w):
        if matrix[i][j] == 'C':
            c.append((i, j))

# sx, sy : 시작지점
# ex, ey : 도착지점
(sx, sy), (ex, ey) = c

visited = [[inf]*w for _ in range(h)]
bfs(sx, sy)

print(visited[ex][ey] - 1)