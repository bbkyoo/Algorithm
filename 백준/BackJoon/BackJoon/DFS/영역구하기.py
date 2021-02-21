# 눈종이의 왼쪽 아래 꼭짓점의 좌표는 (0,0)이고, 오른쪽 위 꼭짓점의 좌표는(N,M)이다. 입력되는 K개의 직사각형들이 모눈종이 전체를 채우는 경우는 없다.
from collections import deque

def bfs(x, y):
    q = deque()
    q.append([x,y])
    matrix[x][y] = 1
    num = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if matrix[nx][ny] == 0:
                    q.append([nx,ny])
                    matrix[nx][ny] = 1
                    num += 1
    
    empty_list.append(num)                    

m,n,k = map(int, input().split())

matrix = [[0]*n for _ in range(m)]
visited = [[0]*n for _ in range(m)]

for _ in range(k):
    left_x, left_y, right_x, right_y = map(int, input().split())
    for i in range(left_y, right_y):
        for j in range(left_x, right_x):
            matrix[i][j] = 1

dx = [1,-1,0,0]
dy = [0,0,1,-1]

empty_list = []
for i in range(m):
    for j in range(n):
        if not matrix[i][j]:
            bfs(i,j)

empty_list.sort()
print(len(empty_list))
print(" ".join(map(str, empty_list)))



