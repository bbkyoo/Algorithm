from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    answer = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and matrix[nx][ny] == 1:
                    q.append([nx, ny])
                    visited[nx][ny] = 1
                    answer += 1
    return answer

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

count = 0
result = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1 and visited[i][j] == 0:
            result = max(result ,bfs(i, j))
            count += 1

print(count)
print(result)













