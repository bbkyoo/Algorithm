# R은 빨강, G는 초록, B는 파랑, P는 보라, Y는 노랑

from collections import deque
import sys

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y, count):

    q = deque()
    q.append([x, y])
    visited = [[0]*6 for _ in range(12)]
    cnt = 1
    visited[x][y] = cnt

    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 12 and 0 <= ny < 6:
                if filed[x][y] == filed[nx][ny] and visited[nx][ny] == 0:
                    cnt += 1
                    q.append([nx, ny])
                    visited[nx][ny] = 1

    if cnt >= 4:
        for i in range(12):
            for j in range(6):
                if visited[i][j] == 1:
                    filed[i][j] = '.'
        count += 1

    return count 

def down():
    for i in range(10, -1, -1):
        for j in range(6):
            if filed[i][j] != '.' and filed[i+1][j] == '.':
                for k in range(i+1, 12):
                    if k == 11 and filed[k][j] == '.':
                        filed[k][j] = filed[i][j]
                    elif filed[k][j] != '.':
                        filed[k-1][j] = filed[i][j]
                        break
                filed[i][j] = '.'

filed = [list(map(str, input().strip())) for _ in range(12)]

ans = 0
while True:
    count = 0
    for i in range(12):
        for j in range(6):
            if filed[i][j] != '.':
                count = bfs(i, j, count)
    
    if count == 0:
        print(ans)
        break
    else:
        ans += 1
    down()








