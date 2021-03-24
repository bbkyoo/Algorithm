# 둘레는 bfs로 풀면 쉽다.

from collections import deque
import sys

input = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,1,0,-1]

n = int(input())

matrix = [[0] * 102 for _ in range(102)]
visited = [[0] * 102 for _ in range(102)]

def bfs(i, j):
    q = deque([])
    visited[i][j] = 1
    q.append([i, j])
    
    answer = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 102 and 0 <= ny < 102:
                if visited[nx][ny] == 0:
                    if matrix[nx][ny]:
                        visited[nx][ny] = 1
                        q.append([nx, ny])
                    else:
                        answer += 1
    return answer

for _ in range(n):
    x, y = map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            if matrix[i][j] == 0:
                matrix[i][j] = 1

ans = 0
for i in range(102):
    for j in range(102):
        if matrix[i][j] and visited[i][j] == 0:
            ans += bfs(i, j)

print(ans)
























