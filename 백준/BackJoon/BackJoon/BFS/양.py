# 글자 '.' (점)은 빈 필드를 의미하며, 글자 '#'는 울타리를, 'o'는 양, 'v'는 늑대
# 양, 늑대의 수
# 양의 수가 늑대의 수보다 많다면 이기고, 늑대를 우리에서 쫓아낸다. 그렇지 않다면 늑대가 그 지역 안의 모든 양을 먹는다.

from collections import deque
import sys

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1 

    ship = 0
    wolf = 0

    if matrix[x][y] == "o":
        ship += 1
    elif matrix[x][y] == "v":
        wolf += 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if visited[nx][ny] == 0 and matrix[nx][ny] != '#':
                    q.append([nx,ny])
                    visited[nx][ny] = 1

                    if matrix[nx][ny] ==  'o':
                        ship += 1
                    elif matrix[nx][ny] ==  'v':
                        wolf += 1
 
    if ship > wolf:
        wolf = 0
    elif ship <= wolf:
        ship = 0

    result = [ship, wolf]

    return result

input = sys.stdin.readline

r, c = map(int, input().split())

matrix =  [ list(map(str, input().strip())) for _ in range(r) ]
visited = [[0]*c for _ in range(r)]

sp = 0
wf = 0

for i in range(r):
    for j in range(c):
        if visited[i][j] == 0 and (matrix[i][j] == "o" or matrix[i][j] == "v"):
            result = bfs(i, j)
            sp += result[0]
            wf += result[1]

print(sp, wf)
            










