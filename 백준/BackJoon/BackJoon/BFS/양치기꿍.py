# 모든 양과 늑대의 수를 계산하고 울타리에서 늑대와 양이 존재할때 (늑대 >= 양, 이면 전체 양 - 울타리에 있던 양) (늑대 < 양, 이면 전체 늑대 - 울타리에 있던 늑대)

from collections import deque
import sys

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    global v, k, tv, tk

    q = deque()
    q.append([x,y])
    visited[x][y] = 1

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if visited[nx][ny] == 0 and matrix[nx][ny] != "#":
                    q.append([nx, ny])
                    visited[nx][ny] = 1

                    if matrix[nx][ny] == "v":
                        tv += 1
                    if matrix[nx][ny] == "k":
                        tk += 1
    
    if tv > 0 and tk > 0:
        if tv >= tk:
            k -= tk
        else:
            v -= tv

r, c = map(int, input().split())

matrix = []
visited = [[0]*c for _ in range(r)]
v = 0
k = 0

for i in range(r):
    line = list(input())
    matrix.append(line)

    for j in range(c):
        if line[j] == 'v':
            v += 1
        elif line[j] == 'k':
            k += 1

for i in range(r):
    for j in range(c):
        if visited[i][j] == 0 and matrix[i][j] != '#':
            tv = 0
            tk = 0
            if matrix[i][j] == "v":
                tv += 1
            elif matrix[i][j] == "k":
                tk += 1
            bfs(i, j)

print(k, v)


















