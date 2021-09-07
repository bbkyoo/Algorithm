# https://chldkato.tistory.com/26

from collections import deque
import sys

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y, cnt):
    q.append([x, y])

    visited[x][y] = cnt

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and matrix[nx][ny] == 1:
                    q.append([nx, ny])
                    visited[nx][ny] = cnt                   
                
def bfs2(num):
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:

                if visited[nx][ny] != num and matrix[nx][ny] == 1:
                    return visited2[x][y] - 1

                if visited2[nx][ny] == 0 and matrix[nx][ny] == 0:
                    visited2[nx][ny] = visited2[x][y] + 1
                    q.append([nx, ny])

n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]* n for _ in range(n)]
q = deque()
q2 = deque()
cnt = 1

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1 and visited[i][j] == 0:
            bfs(i, j, cnt)
            cnt += 1

ans = sys.maxsize
for k in range(1, cnt):
    q = deque()
    visited2 = [[0]* n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1 and visited[i][j] == k:
                q.append([i, j])
                visited2[i][j] = 1

    res = bfs2(k)
    ans = min(ans, res)

print(ans)