# 두 나라의 인구 차이가 L명 이상, R명 이하라면 지나갈수 있다
# 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합
# 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque()
    q.append([x,y])
    temp = []
    visited[x][y] = 1
    temp.append([x,y])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if (abs(matrix[nx][ny] - matrix[x][y])) >= l and (abs(matrix[nx][ny] - matrix[x][y])) <= r:
                    q.append([nx,ny])
                    visited[nx][ny] = 1
                    temp.append([nx,ny])

    return temp


n, l, r = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
while True:
    visited = [[0]*n for _ in range(n)]
    isTrue = False

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                temp = bfs(i,j)
                if len(temp) > 1:
                    isTrue = True
                    num = sum(matrix[x][y] for x, y in temp) // len(temp)
                    for x, y in temp:
                        matrix[x][y] = num
    if not isTrue:
        break
    
    cnt += 1

print(cnt)













