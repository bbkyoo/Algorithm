# 1. 물이 차있을 예정인 곳은 이동하지 못하므로 물을 이동시키고 고슴도치를 이동시키는 순으로 bfs를 수행한다
# 2. 반드시 물은 비버굴에도 이동할 수 없도록 설계해야한다
# 3. 고슴도치가 비버굴에 도착하면 이동한 시간을 출력
# 4. 큐가 비어도 비버굴에 도착하지 못하면 더이상 이동할 수 없으므로 KAKTUS 출력

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(x, y):
    q.append([x, y])
    c[x][y] = 1
    while q:
        qlen = len(q)
        while qlen:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if a[nx][ny] == '.' and c[nx][ny] == 0:
                        c[nx][ny] = c[x][y] + 1
                        q.append([nx, ny])
                    elif a[nx][ny] == 'D':
                        print(c[x][y])
                        return
            qlen -= 1
        water()

    print("KAKTUS")
    return

def water():
    qlen = len(wq)
    while qlen:
        x, y = wq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] == ".":
                    a[nx][ny] = "*"
                    wq.append([nx, ny])
        qlen -= 1

n, m = map(int, input().split())

a = [list(map(str, input())) for i in range(n)]
c = [[0]*m for _ in range(n)]
q, wq = deque(), deque()

for i in range(n):
    for j in range(m):
        if a[i][j] == "S":
            x1, y1 = i, j
            a[i][j] = '.'
        elif a[i][j] == "*":
            wq.append([i, j])

water()
bfs(x1, y1)















