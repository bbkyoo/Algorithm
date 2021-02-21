from collections import deque
import sys

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if visited[nx][ny] == 0 and matrix[nx][ny] == '.':
                    q.append([nx, ny])
                    visited[nx][ny] = 1
                    matrix[nx][ny] = 'O'

def bfs_destroy(x,y):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        matrix[x][y] = '.'

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if visited[nx][ny] == 0 :
                    visited[nx][ny] = 1
                    matrix[nx][ny] = '.'

                    if temp[nx][ny] == 'O':
                        q.append([nx, ny])

input = sys.stdin.readline

r, c, n = map(int, input().split())

matrix = [list(map(str,input().strip())) for _ in range(r)]

for k in range(1,n):
    visited = [[0]*c for _ in range(r)]

    if k % 2 == 1:
        temp = matrix
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == '.' and visited[i][j] == 0:
                    bfs(i,j)
    else:
        for i in range(r):
            for j in range(c):
                if temp[i][j] == 'O' and visited[i][j] == 0:
                    bfs_destroy(i,j)

for i in matrix:
    for j in i:
        print(j, end='')
    print()








        