# 가장 처음에 아기 상어의 크기는 2
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y):
    q = deque([])
    q.append([x, y])
    dist = [[0]*n for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    visited[x][y] = 1
    eat = []

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if matrix[nx][ny] <= matrix[x][y] or matrix[nx][ny] == 0:
                    q.append([nx, ny])
                    visited[nx][ny] = 1
                    dist[nx][ny] = dist[x][y] + 1

                if matrix[nx][ny] < matrix[x][y] and matrix[nx][ny] != 0:
                    eat.append([nx,ny,dist[nx][ny]])

    if not eat:
        return -1, -1 -1
    eat.sort(key=lambda x : (x[2], x[0], x[1]))
    return eat[0][0], eat[0][1], eat[0][2]

n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 9:
            matrix[i][j] = 2
            start = [i, j]

exp = 0
cnt = 0

while True:
    i, j = start[0], start[1]
    ex, ey, dist = bfs(i, j)
    if ex == -1:
        break

    matrix[ex][ey] = matrix[i][j]
    matrix[i][j] = 0
    start = [ex, ey]
    exp += 1
    if exp == matrix[ex][ey]:
        exp = 0
        matrix[ex][ey] += 1
    cnt += dist

print(cnt)









