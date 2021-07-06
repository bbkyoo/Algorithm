from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque([])
    q.append([x, y])
    visited = [[0]*c for _ in range(r)]
    dist = [[0]*c for _ in range(r)]
    visited[x][y] = 1
    dist[x][y] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                if visited[nx][ny] == 0 and matrix[nx][ny] == '.':
                    visited[nx][ny] = 1
                    dist[nx][ny] = dist[x][y] + 1

    answer = 0
    for i in range(len(dist)):
        answer = max(answer , max(dist[i]))

    return answer

r, c= map(int, input().split())

matrix = []
target = 0

for _ in range(r):
    temp = list(input())
    matrix.append(temp)
    for j in range(c):
        if temp[j] == '.':
            target += 1

result = False
for i in range(r):
    for j in range(c):
        if matrix[i][j] == '.':
            if bfs(i, j) == target:
                result = True
                break

print(result)








