from collections import deque
import sys

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    global q, c, ans
    cnt = 0 

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if matrix[nx][ny] == 0 and c[nx][ny] == -1:
                    q.append([nx, ny])
                    c[nx][ny] = c[x][y] + 1
                    cnt = max(cnt, c[nx][ny])
                    
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0 and c[i][j] == -1:
                cnt = sys.maxsize

    ans = min(ans, cnt)


def dfs(index, cnt):
    global q, c, ans
    if cnt == m:
        q = deque()
        c = [[-1]*n for _ in range(n)]
        for i in range(len(arr)):
            if select[i]:
                q.append([arr[i][0], arr[i][1]])
                c[arr[i][0]][arr[i][1]] = 0
        bfs()
        return

    for i in range(index, len(arr)):
        if select[i]:
            continue
        select[i] = 1
        dfs(i+1, cnt+1)
        select[i] = 0


n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
arr = []

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 2:
            arr.append([i,j])
            matrix[i][j] = 0

select = [0 for _ in range(10)]
ans = sys.maxsize
dfs(0,0)

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)