# https://pacific-ocean.tistory.com/352

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
    
    q = deque([])
    q.append([x, y])
    visited = [[0]*m for _ in range(n)]
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and matrix_copy[nx][ny] != 0:
                    matrix_copy[nx][ny] = 0
                    visited[nx][ny] = 1
                    q.append([nx, ny])

def check(i, j):
    cnt = 0
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if matrix_copy[nx][ny] == 0:
                cnt += 1

    return cnt

def checkz():
    for i in range(n):
        for j in range(m):
            if matrix[i][j] != 0:
                return False
    return True

n, m = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

result = 1
while True:
    if checkz():
        print(0)
        break

    matrix_copy = matrix.copy()
    
    for i in range(n):
        for j in range(m):
            if matrix_copy[i][j] != 0:
                temp = matrix[i][j] - check(i,j)
                matrix[i][j] = temp if temp >= 0 else 0
    
    temp = matrix.copy()
    cnt = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] != 0:
                temp[i][j] = 0
                bfs(i, j)
                cnt += 1

    if cnt > 1:
        print(result)
        break

    result += 1





